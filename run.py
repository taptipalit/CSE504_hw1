import os

gcc_popular_flags = ['-fno-strict-aliasing', '-funsigned-char', '-fPIE', '-fsigned-char', '-fno-common', '-fomit-frame-pointer', '-fstack-protector-strong']
clang_popular_flags = ['-fno-string-aliasing', '-fno-signed-char', '-fPIE', '-fsigned-char', '-fno-common', '-momit-leaf-frame-pointer', '-fstack-protector-strong']
gcc_opt_flags = ['-O0', '-O1', '-O2', '-O3', '-Os', '-Ofast']
clang_opt_flags = ['-O0', '-O1', '-O2', '-O3', '-Os']
clang_my_flags = ['-loop-vectorize', '-loop-unroll', '-loop-reroll', '-loop-reduce', '-licm', '-instcombine', '-always-inline']
gcc_my_flags = ['-falign-functions', '-falign-jumps', '-fdce', '-floop-parallelize-all', '-fmove-loop-invariants', '-freorder-functions']


print "Part 1 - Optimization Levels"
# Run optimization level - gcc
for flag in gcc_opt_flags:
    print 'Trying ... GCC ' + flag
    os.system('cp /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def.template /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def')
    os.system("sed -i -e 's/cc/gcc/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")
    os.system("sed -i -e 's/-O3/"+flag+"/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")
    os.chdir('/gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/CG')
    os.system('make CLASS=A > /dev/null 2>&1')
    os.chdir('/gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/bin')
    os.system('./cg.A | grep "Time in seconds"')
    os.system("sed -i -e 's/-O3/"+flag+"/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")

# Run optimization level - clang
for flag in clang_opt_flags:
    print 'Trying ... CLANG ' + flag
    os.system('cp /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def.template /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def')
    os.system("sed -i -e 's/cc/clang/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")
    os.system("sed -i -e 's/-O3/"+flag+"/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")
    os.chdir('/gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/CG')
    os.system('make CLASS=A > /dev/null 2>&1')
    os.chdir('/gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/bin')
    os.system('./cg.A | grep "Time in seconds"')

print "Part 2 - Popular flags"
# Run - gcc
for flag in gcc_popular_flags:
    print 'Trying ... GCC ' + flag
    os.system('cp /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def.template /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def')
    os.system("sed -i -e 's/cc/gcc/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")
    os.system("sed -i -e 's/-O3/"+flag+"/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")
    os.chdir('/gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/CG')
    os.system('make CLASS=A > /dev/null 2>&1')
    os.chdir('/gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/bin')
    os.system('./cg.A | grep "Time in seconds"')
    os.system("sed -i -e 's/-O3/"+flag+"/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")

# Run - clang
for flag in clang_popular_flags:
    print 'Trying ... CLANG ' + flag
    os.system('cp /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def.template /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def')
    os.system("sed -i -e 's/cc/clang/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")
    os.system("sed -i -e 's/-O3/"+flag+"/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")
    os.chdir('/gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/CG')
    os.system('make CLASS=A > /dev/null 2>&1')
    os.chdir('/gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/bin')
    os.system('./cg.A | grep "Time in seconds"')

print 'Part 3 - Selected flags'
# Run - gcc
for flag in gcc_my_flags:
    print 'Trying ... GCC ' + flag
    os.system('cp /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def.template /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def')
    os.system("sed -i -e 's/cc/gcc/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")
    os.system("sed -i -e 's/-O3/"+flag+"/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")
    os.chdir('/gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/CG')
    os.system('make CLASS=A > /dev/null 2>&1')
    os.chdir('/gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/bin')
    os.system('./cg.A | grep "Time in seconds"')
    os.system("sed -i -e 's/-O3/"+flag+"/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")

# Run - clang
for flag in clang_my_flags:
    print 'Trying ... CLANG ' + flag
    os.system('cp /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def.template /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def')
    os.system("sed -i -e 's/cc/clang/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")
    os.system("sed -i -e 's/-O3/"+flag+"/g' /gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/config/make.def")
    os.chdir('/gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/CG')
    os.system('make CLASS=A > /dev/null 2>&1')
    os.chdir('/gpfs/projects/CSE504/tpalit/NPB3.0-omp-C/bin')
    os.system('./cg.A | grep "Time in seconds"')

