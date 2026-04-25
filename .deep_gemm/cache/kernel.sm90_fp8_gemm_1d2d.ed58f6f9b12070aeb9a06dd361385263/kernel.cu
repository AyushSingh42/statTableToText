
#include <deep_gemm/impls/sm90_fp8_gemm_1d2d.cuh>

using namespace deep_gemm;

static void __instantiate_kernel() {
    auto ptr = reinterpret_cast<void*>(&sm90_fp8_gemm_1d2d_impl<
        cute::UMMA::Major::K,
        0, 4096, 2048,
        1,
        16, 32, 128,
        128, 128, 64,
        32, 16,
        128, 128,
        1, 0,
        132, GemmType::Normal,
        EpilogueIdentity
    >);
};
