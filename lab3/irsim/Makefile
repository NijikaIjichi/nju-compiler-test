OBJ_DIR := build
SRCS := irsim.cc main.cc
OBJS := $(patsubst %.cc,$(OBJ_DIR)/%.o,$(SRCS))
BIN  := $(OBJ_DIR)/irsim
CXX  := g++

.DEFAULT_GOAL := $(BIN)
CXXFLAGS := -Iinclude -std=c++17 -O0 -ggdb3 -Wall -MMD
-include $(OBJS:.o=.d)

$(BIN): $(OBJS)
	@echo "+ LNK $@"
	@$(CXX) $^ -o $@

$(OBJ_DIR)/%.o: %.cc
	@echo "+ CC $<"
	@mkdir -p $(@D)
	@$(CXX) -c $(CXXFLAGS) $< -o $@

run: $(BIN)
	@$(BIN) test/sgn.ir

gdb: $(BIN)
	gdb --args $(BIN) test/add.ir

clean:
	rm -rf $(OBJ_DIR)
