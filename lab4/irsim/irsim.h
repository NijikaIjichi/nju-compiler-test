#ifndef IRSIM_H
#define IRSIM_H

#include <array>
#include <cassert>
#include <climits>
#include <iostream>
#include <map>
#include <memory>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace irsim {

template <class T>
int ptr_hi(const T *ptr) {
  return static_cast<int>(
      reinterpret_cast<uintptr_t>(ptr) >> 32);
}

template <class T>
int ptr_lo(const T *ptr) {
  return static_cast<int>(reinterpret_cast<uintptr_t>(ptr));
}

template <class T>
T *lohi_to_ptr(uint32_t lo, uint32_t hi) {
  uintptr_t ptr = ((uint64_t)hi << 32) | lo;
  return reinterpret_cast<T *>(ptr);
}

/* clang-format off */
enum class Exception {
  NONE, IF, LOAD, STORE, DIV_ZERO, OF, TIMEOUT, OOM, ABORT,
  INVOP,
};

enum CtrlRegs {
  CR_RET,    // rw, used for return address
  CR_SERIAL, // read only
  CR_COUNT,  // rw
  CR_ARG,    // rw
};

enum class Opc {
  abort, // as 0
  helper, // native call
  alloca,
  la, ld, st, li, mov, add, sub,
  mul, div, jmp, br, slt, sle, seq, sge, sgt, sne,
  call, ret, mfcr, mtcr, mark,
  quit,
};
/* clang-format on */

using TransitionBlock = std::array<int, 4 * 1024>;

class ProgramInput {
  std::istream *is;
  std::vector<int> *vec;

  friend class Program;

public:
  ProgramInput(std::istream &is) : is(&is), vec(nullptr) {}
  ProgramInput(std::vector<int> &vec)
      : is(nullptr), vec(&vec) {}
  ProgramInput(const ProgramInput &that) = default;

  int read() {
    if (vec) {
      auto ret = vec->back();
      vec->pop_back();
      return ret;
    } else {
      int ret;
      // printf("please input a number: ");
      (*is) >> ret;
      return ret;
    }
  }
};

class ProgramOutput {
  std::ostream *os;
  std::vector<int> *vec;

  friend class Program;

public:
  ProgramOutput(std::ostream &os) : os(&os), vec(nullptr) {}
  ProgramOutput(std::vector<int> &vec)
      : os(nullptr), vec(&vec) {}
  ProgramOutput(const ProgramOutput &that) = default;

  void write(int v) {
    if (vec) {
      vec->push_back(v);
    } else {
      (*os) << v << "\n";
    }
  }
};

class ProgramIO : public ProgramInput,
                  public ProgramOutput {
public:
  ProgramIO(ProgramInput in, ProgramOutput out)
      : ProgramInput(in), ProgramOutput(out) {}
};

template <class T>
class span {
  std::vector<T> &container;
  size_t ptr;
  size_t _size;

public:
  span() : container(*(std::vector<T> *)nullptr) {}
  span(std::vector<T> &container, size_t ptr, size_t size)
      : container(container), ptr(ptr), _size(size) {}

  using iterator = typename std::vector<T>::iterator;
  using const_iterator =
      typename std::vector<T>::const_iterator;

  span(span &&) = default;
  span(const span &) = default;
  span &operator=(span &&) = default;
  span &operator=(const span &) = default;

  void resize(size_t newSize) {
    if (ptr + newSize > container.size())
      throw std::length_error("invalid new size");
    _size = newSize;
  }

  size_t size() const { return _size; }

  iterator begin() { return container.begin() + ptr; }
  const_iterator begin() const {
    return container.begin() + ptr;
  }
  iterator end() { return container.begin() + ptr + _size; }
  const_iterator end() const {
    return container.begin() + ptr + _size;
  }

  T &at(size_t i) {
    if (i >= _size) throw std::range_error("out of range");
    return container.at(ptr + i);
  }
  const T &at(size_t i) const {
    if (i >= _size) throw std::range_error("out of range");
    return container.at(ptr + i);
  }
  T &operator[](size_t i) { return container[ptr + i]; }
  const T &operator[](size_t i) const {
    return container[ptr + i];
  }
};

class Program {
  ProgramIO io;

  unsigned memory_limit = -1u;
  unsigned insts_limit = -1u;

  std::vector<std::unique_ptr<TransitionBlock>> codes;
  TransitionBlock *curblk = nullptr;
  int *textptr = nullptr;
  int *curf = nullptr;

  friend class Compiler;

  /* running environment */
  std::vector<int> args;
  std::vector<int *> frames;
  std::vector<int> memory;
  std::vector<span<int>> stack;
  std::array<uint32_t, 6> ctrl_regs = {};

  Exception exception = Exception::NONE;

public:
  Program() : io(std::cin, std::cout) {
    curblk = new TransitionBlock;
    codes.push_back(
        std::unique_ptr<TransitionBlock>(curblk));
    textptr = &curblk->at(0);

    curf = gen_inst(Opc::quit, 0);
  }

  int run(int *eip);
  void setMemoryLimit(unsigned lim) { memory_limit = lim; }
  void setInstsLimit(unsigned lim) { insts_limit = lim; }
  unsigned getInstCounter() const {
    return ctrl_regs[CR_COUNT];
  }
  Exception getException() const { return exception; }

  void setIO(ProgramIO io) { this->io = io; }
  void setInput(ProgramInput in) {
    static_cast<ProgramInput &>(this->io) = in;
  }
  void setOutput(ProgramOutput out) {
    static_cast<ProgramOutput &>(this->io) = out;
  }

private:
  int *get_textptr() const { return textptr; }
  void check_eof(unsigned N) {
    if (textptr + N + 2 >= &(*curblk)[curblk->size()]) {
      curblk = new TransitionBlock;
      codes.push_back(
          std::unique_ptr<TransitionBlock>(curblk));
      *textptr++ = (int)Opc::jmp;
      *textptr++ = ptr_lo(&(curblk->at(0)));
      *textptr++ = ptr_hi(&(curblk->at(0)));
      textptr = &curblk->at(0);
    }
  }

  template <class... Args>
  int *gen_inst(Opc opc, Args... args) {
    constexpr unsigned N = sizeof...(args);
    check_eof(N + 1);
    auto oldptr = textptr;
    *textptr++ = (int)opc;
    for (int v :
        std::array<int, N>{static_cast<int>(args)...}) {
      *textptr++ = v;
    }

#ifdef DEBUG
    extern std::map<Opc, std::string> opc_to_string;
    printf("+ %p: %s", oldptr, opc_to_string[opc].c_str());
    for (int v :
        std::array<int, N>{static_cast<int>(args)...}) {
      printf(" 0x%x", v);
    }
    printf("\n");
#endif
    return oldptr;
  }

  int *gen_call(int *target) {
    return gen_inst(
        Opc::call, ptr_lo(target), ptr_hi(target));
  }

  int *gen_jmp(int *target) {
    return gen_inst(
        Opc::jmp, ptr_lo(target), ptr_hi(target));
  }

  int *gen_br(int cond, int *target) {
    return gen_inst(
        Opc::br, cond, ptr_lo(target), ptr_hi(target));
  }
};

class Compiler {
  int temp_ptr;
  static constexpr int temp_end = 4;
  int stack_size;
  std::map<std::string, int> vars;
  std::map<std::string, int *> funcs;
  std::map<std::string, int *> labels;
  std::map<int, bool> temps;
  std::map<std::string, std::vector<int *>> backfill_labels;

  static constexpr int m1[] = {1};
  static constexpr int m2[] = {1, 2};
  static constexpr int m3[] = {1, 2, 3};
  static constexpr int m4[] = {1, 2, 3, 4};

  int primary_exp(Program *prog, const std::string &tok,
      int to = INT_MAX);

  using TokenList = std::vector<std::string>;

  bool handle_label(Program *, const TokenList &toks);
  bool handle_func(Program *, const TokenList &toks);
  bool handle_assign(Program *, const TokenList &toks);
  bool handle_arith(Program *, const TokenList &toks);
  bool handle_takeaddr(Program *, const TokenList &toks);
  bool handle_deref(Program *, const TokenList &toks);
  bool handle_deref_assign(
      Program *, const TokenList &toks);
  bool handle_goto_(Program *, const TokenList &toks);
  bool handle_branch(Program *, const TokenList &toks);
  bool handle_ret(Program *, const TokenList &toks);
  bool handle_dec(Program *, const TokenList &toks);
  bool handle_arg(Program *, const TokenList &toks);
  bool handle_call(Program *, const TokenList &toks);
  bool handle_param(Program *, const TokenList &toks);
  bool handle_read(Program *, const TokenList &toks);
  bool handle_write(Program *, const TokenList &toks);

  TokenList splitTokens(const std::string line) {
    std::string tmp;
    std::vector<std::string> out;
    std::istringstream iss(line);
    while (iss >> tmp) out.push_back(tmp);
    return out;
  }

public:
  Compiler() { clear_env(); }

  void clear_env() {
    temp_ptr = 0;
    stack_size = temp_end; // 0 for return value
    vars.clear();
    labels.clear();
  }

  int *getFunction(const std::string &fname) {
    return funcs[fname];
  }

  int getVar(const std::string &name, unsigned size = 1) {
    auto it = vars.find(name);
    if (it == vars.end()) {
      std::tie(it, std::ignore) = vars.insert(
          std::pair<std::string, int>{name, stack_size});
      stack_size += size;
    }
#ifdef DEBUG
    fprintf(stdout, "allocate %d for %s\n", it->second,
        name.c_str());
#endif
    return it->second;
  }

  void clearTemps() { temp_ptr = 0; }

  int newTemp() {
    int tmp = temp_ptr++;
    assert(tmp < temp_end);
    return tmp;
  }

  std::unique_ptr<Program> compile(std::istream &is);
};

} // namespace irsim

#endif
