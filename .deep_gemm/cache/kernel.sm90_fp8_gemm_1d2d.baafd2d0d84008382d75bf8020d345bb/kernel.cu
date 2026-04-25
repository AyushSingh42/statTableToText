
#include <deep_gemm/impls/sm90_fp8_gemm_1d2d.cuh>

using namespace deep_gemm;

static void __instantiate_kernel() {
    auto ptr = reinterpret_cast<void*>(&sm90_fp8_gemm_1d2d_impl<
        cute::UMMA::Major::K,
        0, 2048, 4096,
        1,
        16, 16, 128,
        128, 128, 32,
        32, 0,
        128, 128,
        1, 0,
        132, GemmType::Normal,
        EpilogueIdentity
    >);
};
