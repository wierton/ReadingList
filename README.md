# Reading List of Compiler Testing

# Conference
* ICSE、FSE、ASE
* OSDI、PLDI、POPL、ATC、SOSP、ISSTA

# Journal
* TSE、TOSEM、TOPLAS

# Labels
* Generation: testcase generation, for testing
* Synthesis: construct program/code pieces/DSL and etc
* Bug Localization: find where is possibly the bug
* Symbolic Execution: execute program with symbols and constraints
* Concolic Execution: combine symbolic execution and concrete execution
* Repair: fix program either from compile-time or from runtime
* Fuzzing: randomly generate/manipulate inputs with some heuristic
* Mutation: Mutate existing testcases
* Debugging: help better debugging or related to debugging tools
* Program Comprehension: extract high level summary from program
* Testcase Reduction: reduce testcases' numbers or size
* Testcase Prioritization: reorder testcases to help faster testing
* Verification: manually or automatically give proof to program's properties
* Fomalization: a lot of formulas/symbols, strictly illustrate the complicated (sometimes naive) solutions/problems/concepts
* Performance: improve program's performance, or find performance bugs
* Program Analysis: dynamic or static analysis of program
* Fault Injection: delibrately return rubbish/inconsistent result to program when invoke external api/syscall
* Configuration: detect errors in configuration or test systems which higly depends on configuration
* Regression Testing: as is
* Testing: as is
* Misc Testing: hard to classify
* Refactor: help refactor the code
* Fault Tolarating: runtime mechanism to help program still keep running after fault
* JavaScript: as is
* Web Application: as is
* SMT: satisfiability modulo theory
* Program Slicing:
* Test Acceration: help accelerate some existsing testing methodologies or unit testing/regression testing

# ICSE20
* ICSE20' Ankou: Guiding Grey-box Fuzzing towards Combinatorial Difference
* ICSE20' Automatically Testing String Solvers
* ICSE20' BCFA: Bespoke Control Flow Analysis for CFA at Scale
* ICSE20' Burn After Reading: A Shadow Stack with Microsecond-level Runtime Rerandomization for Protecting Return Addresses
* ICSE20' Causal Testing: Understanding Defects' Root Causes
* ICSE20' Debugging Inputs
* ICSE20' Efficient Generation of Error-Inducing Floating-Point Inputs via Symbolic Execution
* ICSE20' Extracting Taint Specifications for JavaScript Libraries
* ICSE20' HyDiff: Hybrid Differential Software Analysis
* ICSE20' JVM Fuzzing for JIT-Induced Side-Channel Detection
* ICSE20' MemLock: Memory Usage Guided Fuzzing
* ICSE20' Pipelining Bottom-up Data Flow Analysis
* ICSE20' Quickly Generating Diverse Valid Test Inputs with Reinforcement Learning
* ICSE20' SLEMI: Equivalence Modulo Input (EMI) Based Mutation of CPS Models for Finding Compiler Bugs in Simulink
* ICSE20' Securing UnSafe Rust Programs with XRust
* ICSE20' SpecuSym: Speculative Symbolic Execution for Cache Timing Leak Detection
* ICSE20' Symbolic Verification of Message Passing Interface Programs
* ICSE20' Tailoring Programs for Static Analysis via Program Transformation
* ICSE20' Taming Behavioral Backward Incompatibilities via Cross-Project Testing and Analysis
* ICSE20' Targeted Greybox Fuzzing with Static Lookahead Analysis
* ICSE20' Typestate-Guided Fuzzer for Discovering Use-after-Free Vulnerabilities
* ICSE20' Verifying Object Construction
* ICSE20' White-box Fairness Testing through Adversarial Sampling
* ICSE20' sFuzz: An Efficient Adaptive Fuzzer for Solidity Smart Contracts

# FSE20
* FSE20' ARDiff: Scaling Program Equivalence Checking via Iterative Abstraction and Refinement of Common Code
* FSE20' Baital: An Adaptive Weighted Sampling Approach for Improved t-wise Coverage
* FSE20' Block Public Access: Trust Safety Verification of Access Control Policies
* FSE20' Boosting Fuzzer Efficiency: An Information Theoretic Perspective
* FSE20' C2S: Translating Natural Language Comments to Formal Program Specifications
* FSE20' Configuration Smells in Continuous Delivery Pipelines: A Linter and a Six-Month Study on GitLab
* FSE20' Cost Measures Matter for Mutation Testing Study Validity
* FSE20' CrFuzz: Fuzzing Multi-purpose Programs through Input Validation
* FSE20' Detecting Critical Bugs in SMT Solvers Using Blackbox Mutational Fuzzing
* FSE20' Detecting Numerical Bugs in Neural Network Architectures
* FSE20' Detecting Optimization Bugs in Database Engines via Non-optimizing Reference Engine Construction
* FSE20' Detecting and Understanding JavaScript Global Identifier Conflicts on the Web
* FSE20' Dynamically Reconfiguring Software Microbenchmarks: Reducing Execution Time without Sacrificing Result Quality
* FSE20' Efficient Binary-Level Coverage Analysis
* FSE20' Efficiently Finding Higher-Order Mutants
* FSE20' Evolutionary Improvement of Assertion Oracles
* FSE20' Fuzzing: On the Exponential Cost of Vulnerability Discovery
* FSE20' Inductive Program Synthesis over Noisy Data
* FSE20' Intelligent REST API Data Fuzzing
* FSE20' Interval Counterexamples for Loop Invariant Learning
* FSE20' Java Ranger: Statically Summarizing Regions for Efficient Symbolic Execution of Java
* FSE20' Making Symbolic Execution Promising by Learning Aggressive State-Pruning Strategy
* FSE20' Willias: Mining Input Grammars from Dynamic Control Flow
* FSE20' Past-Sensitive Pointer Analysis for Symbolic Execution
* FSE20' UBITect: A Precise and Scalable Method to Detect Use-before-Initialization Bugs in Linux Kernel

# OSDI20
* OSDI20' Specification and verification in the field: Applying formal methods to BPF just-in-time compilers in the Linux kernel
* OSDI20' Determinizing Crash Behavior with a Verified Snapshot-Consistent Flash Translation Layer
* OSDI20' From Global to Local Quiescence: Wait-Free Code Patching of Multi-Threaded Processes
* OSDI20' Testing Database Engines via Pivoted Query Synthesis
* OSDI20' Gauntlet: Finding Bugs in Compilers for Programmable Packet Processing
* OSDI20' Aragog: Scalable Runtime Verification of Shardable Networked Systems
* OSDI20' Automated Reasoning and Detection of Specious Configuration in Large Systems with Symbolic Execution
* OSDI20' Testing Configuration Changes in Context to Prevent Production Failures

# PLDI20
* PLDI20' Armada: Low-Effort Verification of High-Performance Concurrent Programs
* PLDI20' Binary Rewriting without Control Flow Recovery
* PLDI20' BlankIt Library Debloating: Getting What You Want Instead of Cutting What You Don’t
* PLDI20' CARAT: A Case for Virtual Memory through Compiler- and Runtime-Based Address Translation
* PLDI20' Compiler and Runtime Support for Continuation Marks
* PLDI20' Constant-Time Foundations for the New Spectre Era
* PLDI20' Data-Driven Inference of Representation Invariants
* PLDI20' Debug Information Validation for Optimized Code
* PLDI20' Effective Function Merging in the SSA Form
* PLDI20' Efficient Handling of String-Number Conversion
* PLDI20' Exact and Approximate Methods for Proving Unrealizability of Syntax-Guided Synthesis Problems
* PLDI20' Faster General Parsing through Context-Free Memoization
* PLDI20' First-Order Quantified Separators
* PLDI20' Gillian, Part I: A Multi-language Platform for Symbolic Execution
* PLDI20' Learning Fast and Precise Numerical Analysis
* PLDI20' Learning Nonlinear Loop Invariants with Gated Continuous Logic Networks
* PLDI20' Multi-modal Synthesis of Regular Expressions
* PLDI20' OOElala: Order-of-Evaluation Based Alias Analysis for Compiler Optimization
* PLDI20' Optimizing Homomorphic Evaluation Circuits by Program Synthesis and Term Rewriting
* PLDI20' Polynomial Invariant Generation for Non-deterministic Recursive Programs
* PLDI20' Willias: Reconciling Enumerative and Deductive Program Synthesis
* PLDI20' SCAF: A Speculation-Aware Collaborative Dependence Analysis Framework
* PLDI20' Scalable Validation of Binary Lifters
* PLDI20' Templates and Recurrences: Better Together
* PLDI20' The Essence of Bluespec: A Core Language for Rule-Based Hardware Design
* PLDI20' Towards a Verified Range Analysis for JavaScript JITs
* PLDI20' Validating SMT Solvers via Semantic Fusion
* PLDI20' Zippy LL(1) Parsing with Derivatives

# POPL20
* POPL20' Abstract Extensionality: On the Properties of Incomplete Abstract Interpretations
* POPL20' Actris: Session-Type Based Reasoning in Separation Logic
* POPL20' Backpropagation in the Simply Typed Lambda-calculus with Linear Negation
* POPL20' Augmented Example-based Synthesis using Relational Perturbation Properties
* POPL20' Binders by Day, Labels by Night: Effect Instances via Lexically Scoped Handlers
* POPL20' Deductive Verification with Ghost Monitors
* POPL20' Detecting Floating-Point Errors via Atomic Conditions
* POPL20' Formal Verification of a Constant-Time Preserving C Compiler
* POPL20' Incorrectness Logic
* POPL20' Interaction Trees: Representing Recursive and Impure Programs in Coq
* POPL20' Partial Type Constructors: Or, Making Ad Hoc Datatypes Less Ad Hoc
* POPL20' Persistency Semantics of the Intel-x86 Architecture
* POPL20' Willias: Program Synthesis by Type-Guided Abstraction Refinement
* POPL20' Willias: Synthesis of Coordination Programs from Linear Temporal Specifications
* POPL20' Synthesizing Replacement Classes
* POPL20' The Next 700 Relational Program Logics

# ISSTA20
* ISSTA20' Abstracting Failure-Inducing Inputs
* ISSTA20' Fast Bit-Vector Satisfiability
* ISSTA20' How Far We Have Come: Testing Decompilation Correctness of C Decompilers
* ISSTA20' Learning Input Tokens for Effective Fuzzing
* ISSTA20' Patch Based Vulnerability Matching for Binary Programs
* ISSTA20' Relocatable Addressing Model for Symbolic Execution
* ISSTA20' Running Symbolic Execution Forever
* ISSTA20' WEIZZ: Automatic Grey-Box Fuzzing for Structured Binary Formats

# 文法相关
* Stochastic Languages and Stochastic Grammars.
* A Sentence Generator for Testing Parsers
* Compiler testing using a sentence generator
* Using Attributed Grammars to Test Design and Implementations
* Generating Test Data with Enhanced Context-Free Grammars
* The Design and Implementation of a Grammar-Based Data Generator
* The Automatic Generation of Test Cases for Optimizing Fortran Compilers
* Testing syntax and semantic coverage of Java language compilers
* Using Production Grammars in Software Testing
* Testing Attribute Grammars
* Grammar Testing
* Coverage-Driven Automated Compiler Test Suite Generation
* Synthesizing program input grammars

# Oracle
* Practical testing of a C99 compiler using output comparison
* An automatic testing approach for compiler based on metamorphic testing technique
* Metamorphic testing for (graphics) compilers
* RandIR differential testing for embedded compilers
* Randomized stress-testing of link-time optimizers
* Compiler validation via equivalence modulo inputs
* Automatically generating precise Oracles from structured natural language specifications

# 高级版的fuzz
* Find a compiler bug in 5 minutes
* Automated test program generation for an industrial optimizing compiler
* Many-core compiler fuzzing
* Superion grammar-aware greybox fuzzing
* Compiler fuzzing through deep learning
* Automatic Generation of Syntax Valid C Programs for Fuzz Testing
* Finding and understanding bugs in C compilers
* Random testing of C compilers targeting arithmetic optimization
* Reinforcing random testing of arithmetic optimization of C compilers by scaling up size and number of expressions
* Parser-Directed Fuzzing
* Clotho: A Racket Library for Parametric Randomness (Xsmith)

# Mutation
* Finding deep compiler bugs via guided stochastic program mutation
* Evaluating the effects of compiler optimizations on mutation testing at the compiler ir level
* Finding compiler bugs via live code mutation
* Compiler Testing Approach based on Generalized Equivalent Substitution
* Skeletal program enumeration for rigorous compiler testing

# 测试加速/测试约减
* An intermediate representation approach to reducing test suites for retargeted compilers
* An automated approach to reducing test suites for testing retargeted C compilers for embedded systems
* Test-case reduction for C compiler bugs
* Test case prioritization for compilers: a text-vector based approach
* Learning to prioritize test programs for compiler testing
* Learning to accelerate compiler testing
* Coverage Prediction for Accelerating Compiler Testing

# 其它
* Finding missed compiler optimizations by differential testing
* Toward understanding compiler bugs in GCC and LLVM
* Finding and analyzing compiler warning defects
* An Empirical Comparison of Compiler Testing Techniques
* Compiler Fuzzing How Much Does It Matter

# 静态语义
* A Component-Based Formal Language Workbench
* A Constraint Language for Static Semantic Analysis Based on Scope Graphs
* A FORMAL NOTATION FOR SPECIFYING STATIC SEMANTIC RULES
* A General Theory of Syntax with Bindings
* A Theory of Name Resolution
* Executable component-based semantics
* Static Semantic Analysis and Theorem Proving for CASL
* Fuzzing the Rust Typechecker Using CLP
