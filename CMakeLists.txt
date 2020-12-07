include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(PROJECT_NAME $ENV{REZ_BUILD_PROJECT_NAME})
set(PROJECT_VERSION $ENV{REZ_BUILD_PROJECT_VERSION})
set(PROJECT_LIBRARIES ${PROJECT_NAME})

file(MAKE_DIRECTORY ${CMAKE_INSTALL_PREFIX})

set(URL ftp://ftp.gnu.org/gnu/gcc/${PROJECT_NAME}-${PROJECT_VERSION}/${PROJECT_NAME}-${PROJECT_VERSION}.tar.gz)
set(ARCHIVE_REL libs/${PROJECT_NAME}-${PROJECT_VERSION}.tar.gz)

if(NOT EXISTS $ENV{REZ_REPO_PAYLOAD_DIR}/${ARCHIVE_REL})
    message(STATUS "Downloading ${URL}")
    file(DOWNLOAD ${URL} $ENV{REZ_REPO_PAYLOAD_DIR}/${ARCHIVE_REL})
endif()

set(CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-languages=c,c++,fortran --disable-multilib --with-gmp=${REZ_GMP_ROOT} --with-mpc=${REZ_MPC_ROOT} --with-mpfr=${REZ_MPFR_ROOT})
message(status "Configure Command: ${CONFIGURE_COMMAND}")

if(${REZ_BUILD_INSTALL})
	set(INSTALL_COMMAND make -j${REZ_BUILD_THREAD_COUNT} install)
else()
	set(INSTALL_COMMAND ${CMAKE_COMMAND} -E echo "install skipped")
endif()

rez_set_archive(
	ARCHIVE
	${ARCHIVE_REL}
	${URL}
)

ExternalProject_Add(
	${PROJECT_NAME}
	URL ${ARCHIVE}
	UPDATE_COMMAND ""
	CONFIGURE_COMMAND ${CONFIGURE_COMMAND}
	BUILD_IN_SOURCE 1
	BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
	INSTALL_COMMAND ${INSTALL_COMMAND}
)


install(CODE "message(STATUS \"${PROJECT_NAME}-${PROJECT_VERSION} installed.\")")
