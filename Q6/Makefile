CXX = g++
CXXFLAGS = -std=c++17 -Wall -c
LXXFLAGS = -std=c++17
OBJECTS = main.o CGaussSolver.o
TARGET = main


$(TARGET): $(OBJECTS)
	$(CXX) $(LXXFLAGS) $(OBJECTS) -o $(TARGET)
main.o: main.cpp CGaussSolver.cpp
	$(CXX) $(CXXFLAGS) main.cpp
CGaussSolver.o: CGaussSolver.cpp
	$(CXX) $(CXXFLAGS) CGaussSolver.cpp
clean:
	rm -f $(TARGET) $(OBJECTS)
