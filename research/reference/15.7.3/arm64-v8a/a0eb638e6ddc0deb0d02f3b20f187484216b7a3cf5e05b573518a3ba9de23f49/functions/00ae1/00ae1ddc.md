# 00ae1ddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae1d14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1d14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0058.md#compare-40cd7eb1c3d9f6a10ef5e9b0dc49605c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ae1e20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1e20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0007.md#compare-debfd5b0fb126108d1ab2457c08fbf80)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae1ddc",
  "name": "_ZN8firebase9analytics18AddVariantToBundleEP7_JNIEnvP8_jobjectPKcRKNS_7VariantE",
  "size": 816,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17c19a4016e8347a57fb9e67f5b38d8190f6ce74958efefe13c2716967dedda9",
  "source_text_sha256": "17c19a4016e8347a57fb9e67f5b38d8190f6ce74958efefe13c2716967dedda9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae1ddc",
        "00ae210b"
      ]
    ],
    "bytes_sha256": "bca8e2c41e7793e7b5f9d804aa5f6161866e473a589f29d33d0f850b8194a63a",
    "instruction_count": 204,
    "instruction_bytes": 816,
    "body_bytes": 816,
    "indirect": 13,
    "unresolved": 12
  }
}
~~~

## 呼び出し元

- [00bde150](../00bde/00bde150.md)

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bddc60](../00bdd/00bddc60.md)
- [00bddc80](../00bdd/00bddc80.md)
- [00bde090](../00bde/00bde090.md)
- [00bde0c0](../00bde/00bde0c0.md)
- [00bde140](../00bde/00bde140.md)
- [00bde160](../00bde/00bde160.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4040 bytes

~~~c

undefined4
_ZN8firebase9analytics18AddVariantToBundleEP7_JNIEnvP8_jobjectPKcRKNS_7VariantE
          (long *param_1,undefined8 param_2,undefined8 param_3,int *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined1 uVar4;
  byte *pbVar5;
  long lVar6;
  undefined4 uVar7;
  
                    /* try { // try from 00ae1df4 to 00be1dff has its CatchHandler @ 00ae1e14 */
  uVar7 = 0;
                    /* try { // try from 00ae1e00 to 00be1e3f has its CatchHandler @ 00ae1d8c */
                    /* catch() { ... } // from try @ 00ae1df4 with catch @ 00ae1e14 */
                    /* catch() { ... } // from try @ 00ae1dd4 with catch @ 00ae1e28 */
  switch(*param_4) {
  case 0:
    uVar1 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar2 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(5);
    uVar4 = 0;
    break;
  case 1:
    _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE(param_4,1);
    uVar1 = *(undefined8 *)(param_4 + 2);
    uVar2 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar3 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(5);
    FUN_00551e14(param_1,param_2,uVar3,uVar2,uVar1);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb8))(param_1,uVar2);
    return 1;
  case 2:
    _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE(param_4,2);
    uVar3 = *(undefined8 *)(param_4 + 2);
    uVar1 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar2 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(4);
    FUN_00551e14(uVar3,param_1,param_2,uVar2,uVar1);
    goto LAB_00ae1fa0;
  case 3:
    _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE(param_4,3);
    uVar4 = (undefined1)param_4[2];
    uVar1 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar2 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(5);
    break;
  case 4:
  case 5:
  case 10:
    _ZNK8firebase7Variant16assert_is_stringEv(param_4);
    if (*param_4 == 5) {
      pbVar5 = *(byte **)(param_4 + 2);
      if ((*pbVar5 & 1) == 0) {
        pbVar5 = pbVar5 + 1;
      }
      else {
        pbVar5 = *(byte **)(pbVar5 + 0x10);
      }
    }
    else {
      pbVar5 = (byte *)(param_4 + 2);
      if (*param_4 == 4) {
        pbVar5 = *(byte **)pbVar5;
      }
    }
    uVar1 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar2 = (**(code **)(*param_1 + 0x538))(param_1,pbVar5);
    uVar3 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(6);
    FUN_00551e14(param_1,param_2,uVar3,uVar1,uVar2);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb8))(param_1,uVar2);
    goto LAB_00ae20d8;
  case 6:
    _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE(param_4,6);
    uVar1 = _ZN8firebase9analytics23VectorOfMapsToArrayListEP7_JNIEnvRKNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEE
                      (param_1,*(undefined8 *)(param_4 + 2));
    uVar2 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar3 = 8;
    goto LAB_00ae2020;
  case 7:
    _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE(param_4,7);
    uVar1 = _ZN8firebase9analytics11MapToBundleEP7_JNIEnvRKNSt6__ndk13mapINS_7VariantES5_NS3_4lessIS5_EENS3_9allocatorINS3_4pairIKS5_S5_EEEEEE
                      (param_1,*(undefined8 *)(param_4 + 2));
    uVar2 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar3 = 7;
LAB_00ae2020:
    uVar3 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(uVar3);
    FUN_00551e14(param_1,param_2,uVar3,uVar2,uVar1);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb8))(param_1,uVar2);
    lVar6 = *param_1;
    goto LAB_00ae20e4;
  default:
    goto switchD_00ae1e28_caseD_8;
  }
  FUN_00551e14(param_1,param_2,uVar2,uVar1,uVar4);
LAB_00ae1fa0:
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
LAB_00ae20d8:
  lVar6 = *param_1;
LAB_00ae20e4:
  (**(code **)(lVar6 + 0xb8))(param_1,uVar1);
  uVar7 = 1;
switchD_00ae1e28_caseD_8:
  return uVar7;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae1ddc"></a> `00ae1ddc` | `e8 0f 1c fc` | str d8,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00ae1de0"></a> `00ae1de0` | `f7 07 00 f9` | str x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ae1de4"></a> `00ae1de4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae1de8"></a> `00ae1de8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae1dec"></a> `00ae1dec` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ae1df0"></a> `00ae1df0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00ae1df4"></a> `00ae1df4` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-00ae1df8"></a> `00ae1df8` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00ae1dfc"></a> `00ae1dfc` | `1f 29 00 71` | cmp w8,#0xa | `FALL_THROUGH`
<a id="insn-00ae1e00"></a> `00ae1e00` | `88 17 00 54` | b.hi 0x00ae20f0 | `CONDITIONAL_JUMP`
<a id="insn-00ae1e04"></a> `00ae1e04` | `a9 c0 ff 90` | adrp x9,0x2f5000 | `FALL_THROUGH`
<a id="insn-00ae1e08"></a> `00ae1e08` | `29 b5 27 91` | add x9,x9,#0x9ed | `FALL_THROUGH`
<a id="insn-00ae1e0c"></a> `00ae1e0c` | `0a 01 00 10` | adr x10,0xae1e2c | `FALL_THROUGH`
<a id="insn-00ae1e10"></a> `00ae1e10` | `2b 69 68 38` | ldrb w11,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ae1e14"></a> `00ae1e14` | `4a 09 0b 8b` | add x10,x10,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ae1e18"></a> `00ae1e18` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00ae1e1c"></a> `00ae1e1c` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00ae1e20"></a> `00ae1e20` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00ae1e24"></a> `00ae1e24` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae1e28"></a> `00ae1e28` | `40 01 1f d6` | br x10 | `COMPUTED_JUMP`
<a id="insn-00ae1e2c"></a> `00ae1e2c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ae1e30"></a> `00ae1e30` | `94 ef 03 94` | bl 0x00bddc80 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1e34"></a> `00ae1e34` | `e8 02 40 b9` | ldr w8,[x23] | `FALL_THROUGH`
<a id="insn-00ae1e38"></a> `00ae1e38` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00ae1e3c"></a> `00ae1e3c` | `c1 00 00 54` | b.ne 0x00ae1e54 | `CONDITIONAL_JUMP`
<a id="insn-00ae1e40"></a> `00ae1e40` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00ae1e44"></a> `00ae1e44` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00ae1e48"></a> `00ae1e48` | `09 11 00 37` | tbnz w9,#0x0,0x00ae2068 | `CONDITIONAL_JUMP`
<a id="insn-00ae1e4c"></a> `00ae1e4c` | `16 05 00 91` | add x22,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ae1e50"></a> `00ae1e50` | `87 00 00 14` | b 0x00ae206c | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1e54"></a> `00ae1e54` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00ae1e58"></a> `00ae1e58` | `f6 22 00 91` | add x22,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00ae1e5c"></a> `00ae1e5c` | `81 10 00 54` | b.ne 0x00ae206c | `CONDITIONAL_JUMP`
<a id="insn-00ae1e60"></a> `00ae1e60` | `d6 02 40 f9` | ldr x22,[x22] | `FALL_THROUGH`
<a id="insn-00ae1e64"></a> `00ae1e64` | `82 00 00 14` | b 0x00ae206c | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1e68"></a> `00ae1e68` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae1e6c"></a> `00ae1e6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1e70"></a> `00ae1e70` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ae1e74"></a> `00ae1e74` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00ae1e78"></a> `00ae1e78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae1e7c"></a> `00ae1e7c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ae1e80"></a> `00ae1e80` | `a0 00 80 52` | mov w0,#0x5 | `FALL_THROUGH`
<a id="insn-00ae1e84"></a> `00ae1e84` | `8f f0 03 94` | bl 0x00bde0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1e88"></a> `00ae1e88` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00ae1e8c"></a> `00ae1e8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1e90"></a> `00ae1e90` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ae1e94"></a> `00ae1e94` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00ae1e98"></a> `00ae1e98` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00ae1e9c"></a> `00ae1e9c` | `40 00 00 14` | b 0x00ae1f9c | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1ea0"></a> `00ae1ea0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00ae1ea4"></a> `00ae1ea4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ae1ea8"></a> `00ae1ea8` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-00ae1eac"></a> `00ae1eac` | `6d ef 03 94` | bl 0x00bddc60 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1eb0"></a> `00ae1eb0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae1eb4"></a> `00ae1eb4` | `f7 06 40 f9` | ldr x23,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00ae1eb8"></a> `00ae1eb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1ebc"></a> `00ae1ebc` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ae1ec0"></a> `00ae1ec0` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00ae1ec4"></a> `00ae1ec4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae1ec8"></a> `00ae1ec8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ae1ecc"></a> `00ae1ecc` | `a0 00 80 52` | mov w0,#0x5 | `FALL_THROUGH`
<a id="insn-00ae1ed0"></a> `00ae1ed0` | `7c f0 03 94` | bl 0x00bde0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1ed4"></a> `00ae1ed4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00ae1ed8"></a> `00ae1ed8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1edc"></a> `00ae1edc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ae1ee0"></a> `00ae1ee0` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00ae1ee4"></a> `00ae1ee4` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00ae1ee8"></a> `00ae1ee8` | `cb bf e9 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1eec"></a> `00ae1eec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1ef0"></a> `00ae1ef0` | `68 f0 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1ef4"></a> `00ae1ef4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae1ef8"></a> `00ae1ef8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1efc"></a> `00ae1efc` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ae1f00"></a> `00ae1f00` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00ae1f04"></a> `00ae1f04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae1f08"></a> `00ae1f08` | `7a 00 00 14` | b 0x00ae20f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1f0c"></a> `00ae1f0c` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00ae1f10"></a> `00ae1f10` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ae1f14"></a> `00ae1f14` | `53 ef 03 94` | bl 0x00bddc60 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1f18"></a> `00ae1f18` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae1f1c"></a> `00ae1f1c` | `e8 06 40 fd` | ldr d8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00ae1f20"></a> `00ae1f20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1f24"></a> `00ae1f24` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ae1f28"></a> `00ae1f28` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00ae1f2c"></a> `00ae1f2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae1f30"></a> `00ae1f30` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ae1f34"></a> `00ae1f34` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00ae1f38"></a> `00ae1f38` | `62 f0 03 94` | bl 0x00bde0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1f3c"></a> `00ae1f3c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00ae1f40"></a> `00ae1f40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1f44"></a> `00ae1f44` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ae1f48"></a> `00ae1f48` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00ae1f4c"></a> `00ae1f4c` | `00 1d a8 4e` | mov v0.16B,v8.16B | `FALL_THROUGH`
<a id="insn-00ae1f50"></a> `00ae1f50` | `b1 bf e9 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1f54"></a> `00ae1f54` | `13 00 00 14` | b 0x00ae1fa0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1f58"></a> `00ae1f58` | `61 00 80 52` | mov w1,#0x3 | `FALL_THROUGH`
<a id="insn-00ae1f5c"></a> `00ae1f5c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ae1f60"></a> `00ae1f60` | `40 ef 03 94` | bl 0x00bddc60 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1f64"></a> `00ae1f64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae1f68"></a> `00ae1f68` | `f6 22 40 39` | ldrb w22,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00ae1f6c"></a> `00ae1f6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1f70"></a> `00ae1f70` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ae1f74"></a> `00ae1f74` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00ae1f78"></a> `00ae1f78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae1f7c"></a> `00ae1f7c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ae1f80"></a> `00ae1f80` | `a0 00 80 52` | mov w0,#0x5 | `FALL_THROUGH`
<a id="insn-00ae1f84"></a> `00ae1f84` | `4f f0 03 94` | bl 0x00bde0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1f88"></a> `00ae1f88` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00ae1f8c"></a> `00ae1f8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1f90"></a> `00ae1f90` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ae1f94"></a> `00ae1f94` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00ae1f98"></a> `00ae1f98` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00ae1f9c"></a> `00ae1f9c` | `9e bf e9 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1fa0"></a> `00ae1fa0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1fa4"></a> `00ae1fa4` | `3b f0 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1fa8"></a> `00ae1fa8` | `4c 00 00 14` | b 0x00ae20d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1fac"></a> `00ae1fac` | `c1 00 80 52` | mov w1,#0x6 | `FALL_THROUGH`
<a id="insn-00ae1fb0"></a> `00ae1fb0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ae1fb4"></a> `00ae1fb4` | `2b ef 03 94` | bl 0x00bddc60 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1fb8"></a> `00ae1fb8` | `e1 06 40 f9` | ldr x1,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00ae1fbc"></a> `00ae1fbc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1fc0"></a> `00ae1fc0` | `68 f0 03 94` | bl 0x00bde160 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1fc4"></a> `00ae1fc4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae1fc8"></a> `00ae1fc8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ae1fcc"></a> `00ae1fcc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1fd0"></a> `00ae1fd0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ae1fd4"></a> `00ae1fd4` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00ae1fd8"></a> `00ae1fd8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae1fdc"></a> `00ae1fdc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ae1fe0"></a> `00ae1fe0` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00ae1fe4"></a> `00ae1fe4` | `0f 00 00 14` | b 0x00ae2020 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1fe8"></a> `00ae1fe8` | `e1 00 80 52` | mov w1,#0x7 | `FALL_THROUGH`
<a id="insn-00ae1fec"></a> `00ae1fec` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ae1ff0"></a> `00ae1ff0` | `1c ef 03 94` | bl 0x00bddc60 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1ff4"></a> `00ae1ff4` | `e1 06 40 f9` | ldr x1,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00ae1ff8"></a> `00ae1ff8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae1ffc"></a> `00ae1ffc` | `51 f0 03 94` | bl 0x00bde140 | `UNCONDITIONAL_CALL`
<a id="insn-00ae2000"></a> `00ae2000` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae2004"></a> `00ae2004` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ae2008"></a> `00ae2008` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae200c"></a> `00ae200c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ae2010"></a> `00ae2010` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00ae2014"></a> `00ae2014` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae2018"></a> `00ae2018` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ae201c"></a> `00ae201c` | `e0 00 80 52` | mov w0,#0x7 | `FALL_THROUGH`
<a id="insn-00ae2020"></a> `00ae2020` | `28 f0 03 94` | bl 0x00bde0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae2024"></a> `00ae2024` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00ae2028"></a> `00ae2028` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae202c"></a> `00ae202c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ae2030"></a> `00ae2030` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00ae2034"></a> `00ae2034` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00ae2038"></a> `00ae2038` | `77 bf e9 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00ae203c"></a> `00ae203c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae2040"></a> `00ae2040` | `14 f0 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00ae2044"></a> `00ae2044` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae2048"></a> `00ae2048` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae204c"></a> `00ae204c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ae2050"></a> `00ae2050` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00ae2054"></a> `00ae2054` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae2058"></a> `00ae2058` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae205c"></a> `00ae205c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae2060"></a> `00ae2060` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00ae2064"></a> `00ae2064` | `20 00 00 14` | b 0x00ae20e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae2068"></a> `00ae2068` | `16 09 40 f9` | ldr x22,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ae206c"></a> `00ae206c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae2070"></a> `00ae2070` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae2074"></a> `00ae2074` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ae2078"></a> `00ae2078` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00ae207c"></a> `00ae207c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae2080"></a> `00ae2080` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae2084"></a> `00ae2084` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ae2088"></a> `00ae2088` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae208c"></a> `00ae208c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00ae2090"></a> `00ae2090` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00ae2094"></a> `00ae2094` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae2098"></a> `00ae2098` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ae209c"></a> `00ae209c` | `c0 00 80 52` | mov w0,#0x6 | `FALL_THROUGH`
<a id="insn-00ae20a0"></a> `00ae20a0` | `08 f0 03 94` | bl 0x00bde0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae20a4"></a> `00ae20a4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00ae20a8"></a> `00ae20a8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae20ac"></a> `00ae20ac` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ae20b0"></a> `00ae20b0` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00ae20b4"></a> `00ae20b4` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00ae20b8"></a> `00ae20b8` | `57 bf e9 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00ae20bc"></a> `00ae20bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae20c0"></a> `00ae20c0` | `f4 ef 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00ae20c4"></a> `00ae20c4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae20c8"></a> `00ae20c8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae20cc"></a> `00ae20cc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00ae20d0"></a> `00ae20d0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00ae20d4"></a> `00ae20d4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae20d8"></a> `00ae20d8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae20dc"></a> `00ae20dc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae20e0"></a> `00ae20e0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ae20e4"></a> `00ae20e4` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00ae20e8"></a> `00ae20e8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae20ec"></a> `00ae20ec` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-00ae20f0"></a> `00ae20f0` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00ae20f4"></a> `00ae20f4` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ae20f8"></a> `00ae20f8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae20fc"></a> `00ae20fc` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae2100"></a> `00ae2100` | `f7 07 40 f9` | ldr x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ae2104"></a> `00ae2104` | `e8 07 44 fc` | ldr d8,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00ae2108"></a> `00ae2108` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae1ddc`](#insn-00ae1ddc) 範囲 `[['00ae1ddc', '00ae1df3']]`
  - `FALL_THROUGH` [`00ae1df0`](#insn-00ae1df0) → [`00ae1df4`](#insn-00ae1df4)
- ブロック [`00ae1df4`](#insn-00ae1df4) 範囲 `[['00ae1df4', '00ae1dff']]`
  - `FALL_THROUGH` [`00ae1dfc`](#insn-00ae1dfc) → [`00ae1e00`](#insn-00ae1e00)
- ブロック [`00ae1e00`](#insn-00ae1e00) 範囲 `[['00ae1e00', '00ae1e03']]`
  - `CONDITIONAL_JUMP` [`00ae1e00`](#insn-00ae1e00) → [`00ae20f0`](#insn-00ae20f0)
  - `FALL_THROUGH` [`00ae1e00`](#insn-00ae1e00) → [`00ae1e04`](#insn-00ae1e04)
- ブロック [`00ae1e04`](#insn-00ae1e04) 範囲 `[['00ae1e04', '00ae1e13']]`
  - `FALL_THROUGH` [`00ae1e10`](#insn-00ae1e10) → [`00ae1e14`](#insn-00ae1e14)
- ブロック [`00ae1e14`](#insn-00ae1e14) 範囲 `[['00ae1e14', '00ae1e27']]`
  - `FALL_THROUGH` [`00ae1e24`](#insn-00ae1e24) → [`00ae1e28`](#insn-00ae1e28)
- ブロック [`00ae1e28`](#insn-00ae1e28) 範囲 `[['00ae1e28', '00ae1e2b']]`
  - `COMPUTED_JUMP` [`00ae1e28`](#insn-00ae1e28) → [`00ae1e68`](#insn-00ae1e68)
  - `COMPUTED_JUMP` [`00ae1e28`](#insn-00ae1e28) → [`00ae1ea0`](#insn-00ae1ea0)
  - `COMPUTED_JUMP` [`00ae1e28`](#insn-00ae1e28) → [`00ae1f0c`](#insn-00ae1f0c)
  - `COMPUTED_JUMP` [`00ae1e28`](#insn-00ae1e28) → [`00ae1f58`](#insn-00ae1f58)
  - `COMPUTED_JUMP` [`00ae1e28`](#insn-00ae1e28) → [`00ae1e2c`](#insn-00ae1e2c)
  - `COMPUTED_JUMP` [`00ae1e28`](#insn-00ae1e28) → [`00ae1fac`](#insn-00ae1fac)
  - `COMPUTED_JUMP` [`00ae1e28`](#insn-00ae1e28) → [`00ae1fe8`](#insn-00ae1fe8)
  - `COMPUTED_JUMP` [`00ae1e28`](#insn-00ae1e28) → [`00ae20f0`](#insn-00ae20f0)
- ブロック [`00ae1e2c`](#insn-00ae1e2c) 範囲 `[['00ae1e2c', '00ae1e3f']]`
  - `CONDITIONAL_JUMP` [`00ae1e3c`](#insn-00ae1e3c) → [`00ae1e54`](#insn-00ae1e54)
  - `FALL_THROUGH` [`00ae1e3c`](#insn-00ae1e3c) → [`00ae1e40`](#insn-00ae1e40)
- ブロック [`00ae1e40`](#insn-00ae1e40) 範囲 `[['00ae1e40', '00ae1e4b']]`
  - `CONDITIONAL_JUMP` [`00ae1e48`](#insn-00ae1e48) → [`00ae2068`](#insn-00ae2068)
  - `FALL_THROUGH` [`00ae1e48`](#insn-00ae1e48) → [`00ae1e4c`](#insn-00ae1e4c)
- ブロック [`00ae1e4c`](#insn-00ae1e4c) 範囲 `[['00ae1e4c', '00ae1e53']]`
  - `UNCONDITIONAL_JUMP` [`00ae1e50`](#insn-00ae1e50) → [`00ae206c`](#insn-00ae206c)
- ブロック [`00ae1e54`](#insn-00ae1e54) 範囲 `[['00ae1e54', '00ae1e5f']]`
  - `CONDITIONAL_JUMP` [`00ae1e5c`](#insn-00ae1e5c) → [`00ae206c`](#insn-00ae206c)
  - `FALL_THROUGH` [`00ae1e5c`](#insn-00ae1e5c) → [`00ae1e60`](#insn-00ae1e60)
- ブロック [`00ae1e60`](#insn-00ae1e60) 範囲 `[['00ae1e60', '00ae1e67']]`
  - `UNCONDITIONAL_JUMP` [`00ae1e64`](#insn-00ae1e64) → [`00ae206c`](#insn-00ae206c)
- ブロック [`00ae1e68`](#insn-00ae1e68) 範囲 `[['00ae1e68', '00ae1e9f']]`
  - `UNCONDITIONAL_JUMP` [`00ae1e9c`](#insn-00ae1e9c) → [`00ae1f9c`](#insn-00ae1f9c)
- ブロック [`00ae1ea0`](#insn-00ae1ea0) 範囲 `[['00ae1ea0', '00ae1f0b']]`
  - `UNCONDITIONAL_JUMP` [`00ae1f08`](#insn-00ae1f08) → [`00ae20f0`](#insn-00ae20f0)
- ブロック [`00ae1f0c`](#insn-00ae1f0c) 範囲 `[['00ae1f0c', '00ae1f57']]`
  - `UNCONDITIONAL_JUMP` [`00ae1f54`](#insn-00ae1f54) → [`00ae1fa0`](#insn-00ae1fa0)
- ブロック [`00ae1f58`](#insn-00ae1f58) 範囲 `[['00ae1f58', '00ae1f9b']]`
  - `FALL_THROUGH` [`00ae1f98`](#insn-00ae1f98) → [`00ae1f9c`](#insn-00ae1f9c)
- ブロック [`00ae1f9c`](#insn-00ae1f9c) 範囲 `[['00ae1f9c', '00ae1f9f']]`
  - `FALL_THROUGH` [`00ae1f9c`](#insn-00ae1f9c) → [`00ae1fa0`](#insn-00ae1fa0)
- ブロック [`00ae1fa0`](#insn-00ae1fa0) 範囲 `[['00ae1fa0', '00ae1fab']]`
  - `UNCONDITIONAL_JUMP` [`00ae1fa8`](#insn-00ae1fa8) → [`00ae20d8`](#insn-00ae20d8)
- ブロック [`00ae1fac`](#insn-00ae1fac) 範囲 `[['00ae1fac', '00ae1fe7']]`
  - `UNCONDITIONAL_JUMP` [`00ae1fe4`](#insn-00ae1fe4) → [`00ae2020`](#insn-00ae2020)
- ブロック [`00ae1fe8`](#insn-00ae1fe8) 範囲 `[['00ae1fe8', '00ae201f']]`
  - `FALL_THROUGH` [`00ae201c`](#insn-00ae201c) → [`00ae2020`](#insn-00ae2020)
- ブロック [`00ae2020`](#insn-00ae2020) 範囲 `[['00ae2020', '00ae2067']]`
  - `UNCONDITIONAL_JUMP` [`00ae2064`](#insn-00ae2064) → [`00ae20e4`](#insn-00ae20e4)
- ブロック [`00ae2068`](#insn-00ae2068) 範囲 `[['00ae2068', '00ae206b']]`
  - `FALL_THROUGH` [`00ae2068`](#insn-00ae2068) → [`00ae206c`](#insn-00ae206c)
- ブロック [`00ae206c`](#insn-00ae206c) 範囲 `[['00ae206c', '00ae20d7']]`
  - `FALL_THROUGH` [`00ae20d4`](#insn-00ae20d4) → [`00ae20d8`](#insn-00ae20d8)
- ブロック [`00ae20d8`](#insn-00ae20d8) 範囲 `[['00ae20d8', '00ae20e3']]`
  - `FALL_THROUGH` [`00ae20e0`](#insn-00ae20e0) → [`00ae20e4`](#insn-00ae20e4)
- ブロック [`00ae20e4`](#insn-00ae20e4) 範囲 `[['00ae20e4', '00ae20ef']]`
  - `FALL_THROUGH` [`00ae20ec`](#insn-00ae20ec) → [`00ae20f0`](#insn-00ae20f0)
- ブロック [`00ae20f0`](#insn-00ae20f0) 範囲 `[['00ae20f0', '00ae210b']]`

## 命令位置別の参照

- [`00ae1ddc`](#insn-00ae1ddc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1de0`](#insn-00ae1de0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1de4`](#insn-00ae1de4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1de8`](#insn-00ae1de8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1dec`](#insn-00ae1dec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e00`](#insn-00ae1e00) → [`00ae20f0`](#insn-00ae20f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00ae1e28::caseD_8` · 推定型 `None`
- [`00ae1e10`](#insn-00ae1e10) → `002f59ed`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00ae1e28::switchdataD_002f59ed` · 推定型 `byte`
- [`00ae1e28`](#insn-00ae1e28) → [`00ae1e68`](#insn-00ae1e68) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00ae1e28::caseD_0` · 推定型 `None`
- [`00ae1e28`](#insn-00ae1e28) → [`00ae1ea0`](#insn-00ae1ea0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00ae1e28::caseD_1` · 推定型 `None`
- [`00ae1e28`](#insn-00ae1e28) → [`00ae1f0c`](#insn-00ae1f0c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00ae1e28::caseD_2` · 推定型 `None`
- [`00ae1e28`](#insn-00ae1e28) → [`00ae1f58`](#insn-00ae1f58) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00ae1e28::caseD_3` · 推定型 `None`
- [`00ae1e28`](#insn-00ae1e28) → [`00ae1e2c`](#insn-00ae1e2c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00ae1e28::caseD_4` · 推定型 `None`
- [`00ae1e28`](#insn-00ae1e28) → [`00ae1fac`](#insn-00ae1fac) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00ae1e28::caseD_6` · 推定型 `None`
- [`00ae1e28`](#insn-00ae1e28) → [`00ae1fe8`](#insn-00ae1fe8) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00ae1e28::caseD_7` · 推定型 `None`
- [`00ae1e28`](#insn-00ae1e28) → [`00ae20f0`](#insn-00ae20f0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00ae1e28::caseD_8` · 推定型 `None`
- [`00ae1e30`](#insn-00ae1e30) → [`00bddc80`](../00bdd/00bddc80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc80` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e3c`](#insn-00ae1e3c) → [`00ae1e54`](#insn-00ae1e54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e48`](#insn-00ae1e48) → [`00ae2068`](#insn-00ae2068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e50`](#insn-00ae1e50) → [`00ae206c`](#insn-00ae206c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e5c`](#insn-00ae1e5c) → [`00ae206c`](#insn-00ae206c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e64`](#insn-00ae1e64) → [`00ae206c`](#insn-00ae206c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e84`](#insn-00ae1e84) → [`00bde0c0`](../00bde/00bde0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0c0` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e9c`](#insn-00ae1e9c) → [`00ae1f9c`](#insn-00ae1f9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1eac`](#insn-00ae1eac) → [`00bddc60`](../00bdd/00bddc60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc60` · 推定シンボル `None` · 推定型 `None`
- [`00ae1ed0`](#insn-00ae1ed0) → [`00bde0c0`](../00bde/00bde0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0c0` · 推定シンボル `None` · 推定型 `None`
- [`00ae1ee8`](#insn-00ae1ee8) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00ae1ef0`](#insn-00ae1ef0) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f08`](#insn-00ae1f08) → [`00ae20f0`](#insn-00ae20f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00ae1e28::caseD_8` · 推定型 `None`
- [`00ae1f14`](#insn-00ae1f14) → [`00bddc60`](../00bdd/00bddc60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc60` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f38`](#insn-00ae1f38) → [`00bde0c0`](../00bde/00bde0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0c0` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f50`](#insn-00ae1f50) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f54`](#insn-00ae1f54) → [`00ae1fa0`](#insn-00ae1fa0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f60`](#insn-00ae1f60) → [`00bddc60`](../00bdd/00bddc60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc60` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f84`](#insn-00ae1f84) → [`00bde0c0`](../00bde/00bde0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0c0` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f9c`](#insn-00ae1f9c) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00ae1fa4`](#insn-00ae1fa4) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00ae1fa8`](#insn-00ae1fa8) → [`00ae20d8`](#insn-00ae20d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1fb4`](#insn-00ae1fb4) → [`00bddc60`](../00bdd/00bddc60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc60` · 推定シンボル `None` · 推定型 `None`
- [`00ae1fc0`](#insn-00ae1fc0) → [`00bde160`](../00bde/00bde160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde160` · 推定シンボル `None` · 推定型 `None`
- [`00ae1fe4`](#insn-00ae1fe4) → [`00ae2020`](#insn-00ae2020) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1ff0`](#insn-00ae1ff0) → [`00bddc60`](../00bdd/00bddc60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc60` · 推定シンボル `None` · 推定型 `None`
- [`00ae1ffc`](#insn-00ae1ffc) → [`00bde140`](../00bde/00bde140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde140` · 推定シンボル `None` · 推定型 `None`
- [`00ae2020`](#insn-00ae2020) → [`00bde0c0`](../00bde/00bde0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0c0` · 推定シンボル `None` · 推定型 `None`
- [`00ae2038`](#insn-00ae2038) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00ae2040`](#insn-00ae2040) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00ae2064`](#insn-00ae2064) → [`00ae20e4`](#insn-00ae20e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20a0`](#insn-00ae20a0) → [`00bde0c0`](../00bde/00bde0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0c0` · 推定シンボル `None` · 推定型 `None`
- [`00ae20b8`](#insn-00ae20b8) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00ae20c0`](#insn-00ae20c0) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00ae20f4`](#insn-00ae20f4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20f8`](#insn-00ae20f8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20fc`](#insn-00ae20fc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2100`](#insn-00ae2100) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae1ddc`](#insn-00ae1ddc)

~~~json
{
  "source": "00ae1ddc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1de0`](#insn-00ae1de0)

~~~json
{
  "source": "00ae1de0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1de4`](#insn-00ae1de4)

~~~json
{
  "source": "00ae1de4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1de8`](#insn-00ae1de8)

~~~json
{
  "source": "00ae1de8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1dec`](#insn-00ae1dec)

~~~json
{
  "source": "00ae1dec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e00`](#insn-00ae1e00)

~~~json
{
  "source": "00ae1e00",
  "target": "00ae20f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e10`](#insn-00ae1e10)

~~~json
{
  "source": "00ae1e10",
  "target": "002f59ed",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002f59ed",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "0f",
  "capture_start": "002f59ed",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae1e28`](#insn-00ae1e28)

~~~json
{
  "source": "00ae1e28",
  "target": "00ae1e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e28`](#insn-00ae1e28)

~~~json
{
  "source": "00ae1e28",
  "target": "00ae1ea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e28`](#insn-00ae1e28)

~~~json
{
  "source": "00ae1e28",
  "target": "00ae1f0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e28`](#insn-00ae1e28)

~~~json
{
  "source": "00ae1e28",
  "target": "00ae1f58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e28`](#insn-00ae1e28)

~~~json
{
  "source": "00ae1e28",
  "target": "00ae1e2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e28`](#insn-00ae1e28)

~~~json
{
  "source": "00ae1e28",
  "target": "00ae1fac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e28`](#insn-00ae1e28)

~~~json
{
  "source": "00ae1e28",
  "target": "00ae1fe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e28`](#insn-00ae1e28)

~~~json
{
  "source": "00ae1e28",
  "target": "00ae20f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e30`](#insn-00ae1e30)

~~~json
{
  "source": "00ae1e30",
  "target": "00bddc80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1e3c`](#insn-00ae1e3c)

~~~json
{
  "source": "00ae1e3c",
  "target": "00ae1e54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e48`](#insn-00ae1e48)

~~~json
{
  "source": "00ae1e48",
  "target": "00ae2068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e50`](#insn-00ae1e50)

~~~json
{
  "source": "00ae1e50",
  "target": "00ae206c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e5c`](#insn-00ae1e5c)

~~~json
{
  "source": "00ae1e5c",
  "target": "00ae206c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e64`](#insn-00ae1e64)

~~~json
{
  "source": "00ae1e64",
  "target": "00ae206c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e84`](#insn-00ae1e84)

~~~json
{
  "source": "00ae1e84",
  "target": "00bde0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1e9c`](#insn-00ae1e9c)

~~~json
{
  "source": "00ae1e9c",
  "target": "00ae1f9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1eac`](#insn-00ae1eac)

~~~json
{
  "source": "00ae1eac",
  "target": "00bddc60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1ed0`](#insn-00ae1ed0)

~~~json
{
  "source": "00ae1ed0",
  "target": "00bde0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1ee8`](#insn-00ae1ee8)

~~~json
{
  "source": "00ae1ee8",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1ef0`](#insn-00ae1ef0)

~~~json
{
  "source": "00ae1ef0",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1f08`](#insn-00ae1f08)

~~~json
{
  "source": "00ae1f08",
  "target": "00ae20f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f14`](#insn-00ae1f14)

~~~json
{
  "source": "00ae1f14",
  "target": "00bddc60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1f38`](#insn-00ae1f38)

~~~json
{
  "source": "00ae1f38",
  "target": "00bde0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1f50`](#insn-00ae1f50)

~~~json
{
  "source": "00ae1f50",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1f54`](#insn-00ae1f54)

~~~json
{
  "source": "00ae1f54",
  "target": "00ae1fa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f60`](#insn-00ae1f60)

~~~json
{
  "source": "00ae1f60",
  "target": "00bddc60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1f84`](#insn-00ae1f84)

~~~json
{
  "source": "00ae1f84",
  "target": "00bde0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1f9c`](#insn-00ae1f9c)

~~~json
{
  "source": "00ae1f9c",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1fa4`](#insn-00ae1fa4)

~~~json
{
  "source": "00ae1fa4",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1fa8`](#insn-00ae1fa8)

~~~json
{
  "source": "00ae1fa8",
  "target": "00ae20d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1fb4`](#insn-00ae1fb4)

~~~json
{
  "source": "00ae1fb4",
  "target": "00bddc60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1fc0`](#insn-00ae1fc0)

~~~json
{
  "source": "00ae1fc0",
  "target": "00bde160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1fe4`](#insn-00ae1fe4)

~~~json
{
  "source": "00ae1fe4",
  "target": "00ae2020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1ff0`](#insn-00ae1ff0)

~~~json
{
  "source": "00ae1ff0",
  "target": "00bddc60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1ffc`](#insn-00ae1ffc)

~~~json
{
  "source": "00ae1ffc",
  "target": "00bde140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae2020`](#insn-00ae2020)

~~~json
{
  "source": "00ae2020",
  "target": "00bde0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae2038`](#insn-00ae2038)

~~~json
{
  "source": "00ae2038",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae2040`](#insn-00ae2040)

~~~json
{
  "source": "00ae2040",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae2064`](#insn-00ae2064)

~~~json
{
  "source": "00ae2064",
  "target": "00ae20e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20a0`](#insn-00ae20a0)

~~~json
{
  "source": "00ae20a0",
  "target": "00bde0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae20b8`](#insn-00ae20b8)

~~~json
{
  "source": "00ae20b8",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae20c0`](#insn-00ae20c0)

~~~json
{
  "source": "00ae20c0",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae20f4`](#insn-00ae20f4)

~~~json
{
  "source": "00ae20f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20f8`](#insn-00ae20f8)

~~~json
{
  "source": "00ae20f8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20fc`](#insn-00ae20fc)

~~~json
{
  "source": "00ae20fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2100`](#insn-00ae2100)

~~~json
{
  "source": "00ae2100",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
