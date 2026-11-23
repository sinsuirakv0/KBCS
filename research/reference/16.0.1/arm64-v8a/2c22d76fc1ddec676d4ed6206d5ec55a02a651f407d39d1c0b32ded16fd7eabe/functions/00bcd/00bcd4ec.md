# 00bcd4ec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcd0c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd0c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0081.md#compare-a1ba4bd0e55e291e64dfb104f4b3484a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0091.md#compare-4920aa021a411e079161a02653e7c2ad)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcd4ec",
  "name": "_ZN8firebase4auth13CheckEmulatorEPNS0_8AuthDataE",
  "size": 328,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cbf095072252d4b5722aa06a8b97f1cd61eb116cf3a6ec2997a5bfb3c6ca40af",
  "source_text_sha256": "cbf095072252d4b5722aa06a8b97f1cd61eb116cf3a6ec2997a5bfb3c6ca40af"
}
~~~

## 呼び出し元

- [00c5dc20](../00c5d/00c5dc20.md)

## 呼び出し先

- [00574cec](../00574/00574cec.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58060](../00c58/00c58060.md)
- [00c598a0](../00c59/00c598a0.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5afe0](../00c5a/00c5afe0.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b5c0](../00c5b/00c5b5c0.md)

## 関連文字列（未確認候補）

~~~text
"10.0.2.2"
"9099"
"AUTH_EMULATOR_PORT"
"USE_AUTH_EMULATOR"
"Using Auth Emulator for testing."
"Using Auth Prod for testing."
~~~

## 疑似コード / UTF-8 1957 bytes

~~~c

void _ZN8firebase4auth13CheckEmulatorEPNS0_8AuthDataE(undefined8 *param_1)

{
  long lVar1;
  undefined4 uVar2;
  char *pcVar3;
  long *plVar4;
  undefined8 uVar5;
  byte local_50 [16];
  void *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  pcVar3 = getenv("USE_AUTH_EMULATOR");
  if (pcVar3 == (char *)0x0) {
    _ZN8firebase7LogInfoEPKcz("Using Auth Prod for testing.");
  }
  else {
    _ZN8firebase7LogInfoEPKcz("Using Auth Emulator for testing.");
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
              (local_50,&DAT_002bd456);
                    /* try { // try from 00bcd540 to 00ccd54b has its CatchHandler @ 00bce8e4 */
    uVar2 = _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
                      (local_50,0,10);
    if ((local_50[0] & 1) != 0) {
      _ZdlPv(local_40);
    }
                    /* try { // try from 00bcd560 to 00ccd563 has its CatchHandler @ 00bce888 */
                    /* try { // try from 00bcd564 to 00ccd88f has its CatchHandler @ 00bcc5d0 */
    pcVar3 = getenv("AUTH_EMULATOR_PORT");
    if (pcVar3 != (char *)0x0) {
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc(local_50,pcVar3);
      uVar2 = _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
                        (local_50,0,10);
      if ((local_50[0] & 1) != 0) {
        _ZdlPv(local_40);
      }
    }
    plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
    uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,"10.0.2.2");
    FUN_00574cec(plVar4,param_1[0x3f],DAT_01126788,uVar5,uVar2);
    (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar4);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
