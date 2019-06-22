# compiler_viewer

Instantly compile and show output of c++ project for quick feedback.

* Press \<F5> in vim to force reload
* Press \<F1> to jump to errors
* Best experience with tmux

## Modes
* Interactive mode
  * Requirements: gcc compiler
  * Allows for quick build and testing of small programs
  * Suppors linking against header only libs
* Developer mode
  * Requirements: makefiles
  * Create a lib, test and build continiously for quick feedback

## Features
* Error parsing
  * Parsing errors for ease of readability

* Disassembler
  * View disassembly on the fly

* Instant compilation

## Command line args
*  -c , --config CONFIG
    * Provide a config path conf
    * If file doesn't exist a config is created with the given cmd line args
    * If file exists the file is used and overrides the cmd line args
*  -m , --mode MODE
    * Developer (d | developer)
    * Use with a project with make files, uses make to build project
    * Interactive (i | interactive)
    * Use for quick feedback to link against a header only project
    * If no include lib is provided a blank c++ test is created and built
    * Uses gcc as the compiler
*  -p , --project-dir PROJECT_DIR
    * Path to project home dir, it is used to watch all files (with extention: cpp, hpp, h, c) under the directory for changes 
*  -i , --include-dir [INCLUDE_DIR [INCLUDE_DIR ...]]
    * Interactive mode only: path to lib dir used to link when running. adds "-I INCLUDE_DIR" option to gcc when building
*  -b , --build-dir BUILD_DIR
    * Developer mode only: relative path from project dir, or absolute path. Must be directory with makefiles
*  -a , --asm ASM
    * In interactive mode: use only '-a' to generate assembly ()
    * In developer mode: use -a <name_of_obj_file> (used to recurcively search for file inside the project dir)
*  -f , --build-flags [BUILD_FLAGS [BUILD_FLAGS ...]]
    * Used to pass flags to make and gcc, provide flags without '-' 
*  -of , --objdump-flags [OBJDUMP_FLAGS [OBJDUMP_FLAGS ...]]
    * Used to pass flags to objdump

## Screenshots
![Alt text](/docs/compiler_viewer_developer_asm.PNG/?raw=true "Developer Mode ASM")
![Alt text](/docs/compiler_viewer_developer_error.PNG/?raw=true "Developer Mode ERROR")
