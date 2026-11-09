# 004adbdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "004adbdc",
  "name": "_ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "af66e4a8d7157c1dab53fbedfb73a780f0133f68fcd864e3e11354f8814a0f54",
  "source_text_sha256": "af66e4a8d7157c1dab53fbedfb73a780f0133f68fcd864e3e11354f8814a0f54"
}
~~~

## 呼び出し元

- [00c59670](../00c59/00c59670.md)

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)
- [00c585a0](../00c58/00c585a0.md)
- [00c585b0](../00c58/00c585b0.md)

## 疑似コード / UTF-8 1245 bytes

~~~c

void _ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE
               (long *param_1,undefined8 param_2)

{
  long lVar1;
  undefined4 uVar2;
  undefined1 auVar3 [16];
  undefined1 local_70 [16];
  int local_60;
  int iStack_5c;
  time_t local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  *param_1 = (long)(PTR__ZTVN5Botan9X509_TimeE_00c9a9b0 + 0x10);
  param_1[1] = 0;
  param_1[2] = 0;
  param_1[3] = 0;
  *(undefined4 *)(param_1 + 4) = 0xff00;
  local_30 = _ZNSt6__ndk16chrono12system_clock9to_time_tERKNS0_10time_pointIS1_NS0_8durationIxNS_5ratioILl1ELl1000000EEEEEEE
                       (param_2);
  gmtime_r(&local_30,(tm *)local_70);
  auVar3 = NEON_rev64(local_70,4);
  *(uint *)(param_1 + 1) = iStack_5c + 0x76cU;
  *(int *)((long)param_1 + 0xc) = local_60 + 1;
  auVar3 = NEON_ext(auVar3,auVar3,8,1);
  uVar2 = 0x17;
  if (0x801 < iStack_5c + 0x76cU) {
    uVar2 = 0x18;
  }
  *(undefined4 *)(param_1 + 4) = uVar2;
  param_1[3] = auVar3._8_8_;
  param_1[2] = auVar3._0_8_;
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
