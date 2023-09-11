#include "irsim.h"

#include <fstream>
#include <stdio.h>
#include <string>

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

int main(int argc, const char *argv[]) {
  if (argc <= 1) {
    eprintf("usage: irsim [*.ir]\n");
    return 0;
  }

  std::ifstream ifs(argv[1]);

  if (!ifs.good()) {
    eprintf("'%s' no such file\n", argv[1]);
    return 0;
  }

  using namespace irsim;
  Compiler compiler;
  auto prog = compiler.compile(ifs);
  prog->setInstsLimit(100000000);
  prog->setMemoryLimit(128 * 1024 * 1024);
  auto *entry = compiler.getFunction("main");
  if (!entry) {
    eprintf("no main in %s\n", argv[1]);
    return 0;
  }

  auto code = prog->run(entry);
  if (code == 0 ||
      prog->getException() == Exception::NONE) {
    printf("return %d, execute %d instructions\n", code,
        prog->getInstCounter());
  } else {
    switch (prog->getException()) {
    case Exception::IF:
      eprintf(
          "fetch instruction error (labels used but not "
          "defined)\n");
      break;
    case Exception::LOAD:
      eprintf("memory load exception\n");
      break;
    case Exception::STORE:
      eprintf("memory store exception\n");
      break;
    case Exception::DIV_ZERO:
      eprintf("divided by zero exception\n");
      break;
    case Exception::OF:
      eprintf("divide INT_MIN by -1 exception\n");
      break;
    case Exception::TIMEOUT:
      eprintf("run out of instructions\n");
      break;
    case Exception::OOM:
      eprintf("run out of memory\n");
      break;
    case Exception::ABORT:
      eprintf("abort (function not return)\n");
      break;
    case Exception::INVOP:
      eprintf("invalid instruction (bug of irsim)\n");
      break;
    default: break;
    }
  }
  return 0;
}
