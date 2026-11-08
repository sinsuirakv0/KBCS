# 00bdcfb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bdcfb0",
  "name": "_ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7_ISE_EEEENS1_6chrono10time_pointINSJ_12system_clockENSJ_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "81159988e6d9291fae76616c39a295ba8d8e6d5f2eace1d5fc1b4413ab14d219",
  "source_text_sha256": "81159988e6d9291fae76616c39a295ba8d8e6d5f2eace1d5fc1b4413ab14d219"
}
~~~

## 呼び出し元

- [005060a8](../00506/005060a8.md)

## 呼び出し先

- [005054cc](../00505/005054cc.md)

## 疑似コード / UTF-8 656 bytes

~~~c

void _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7_ISE_EEEENS1_6chrono10time_pointINSJ_12system_clockENSJ_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE
               (void)

{
                    /* try { // try from 00bdcfb0 to 00cdd21b has its CatchHandler @ 00bdcbcc */
  (*(code *)
    PTR__ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7_ISE_EEEENS1_6chrono10time_pointINSJ_12system_clockENSJ_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE_00c1d010
  )();
  return;
}

~~~
