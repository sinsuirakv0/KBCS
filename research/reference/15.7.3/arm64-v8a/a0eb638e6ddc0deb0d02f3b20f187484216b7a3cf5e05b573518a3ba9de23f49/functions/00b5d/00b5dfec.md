# 00b5dfec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b5df24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5df24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0069.md#compare-0e5219fdbefb19679a8f83932ac5875c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5e030`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e030.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0070.md#compare-5f5685676d55741381f9f487248363ec)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5dfec",
  "name": "_ZN8firebase4auth4Auth19DestroyPlatformAuthEPNS0_8AuthDataE",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f669ae4506e50bb5b7fc09e97699815408f60940c7686f640c42a96f3dfef8df",
  "source_text_sha256": "f669ae4506e50bb5b7fc09e97699815408f60940c7686f640c42a96f3dfef8df",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5dfec",
        "00b5e147"
      ]
    ],
    "bytes_sha256": "7dfefedb87cc77a123fb767a3908e0a9eaec41e70f78e3ae245d78db8a57bfe6",
    "instruction_count": 87,
    "instruction_bytes": 348,
    "body_bytes": 348,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be0a00](../00be0/00be0a00.md)

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bde030](../00bde/00bde030.md)
- [00bde100](../00bde/00bde100.md)
- [00bde130](../00bde/00bde130.md)
- [00bde1b0](../00bde/00bde1b0.md)
- [00be0c10](../00be0/00be0c10.md)
- [00be0c20](../00be0/00be0c20.md)
- [00be0c30](../00be0/00be0c30.md)
- [00be0c50](../00be0/00be0c50.md)
- [00be0c70](../00be0/00be0c70.md)

## 関連文字列（未確認候補）

~~~text
"g_initialized_count"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1841 bytes

~~~c

void _ZN8firebase4auth4Auth19DestroyPlatformAuthEPNS0_8AuthDataE
               (undefined8 param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  long lVar2;
  
                    /* try { // try from 00b5dfec to 00c5dff7 has its CatchHandler @ 00b5e558 */
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*param_2);
  if ((*(byte *)(param_2 + 0x28) & 1) == 0) {
    lVar2 = (long)param_2 + 0x141;
  }
  else {
    lVar2 = param_2[0x2a];
  }
  _ZN8firebase4util15CancelCallbacksEP7_JNIEnvPKc(uVar1,lVar2);
                    /* try { // try from 00b5e044 to 00c5e067 has its CatchHandler @ 00b5e560 */
  FUN_00551e14(uVar1,param_2[0x41],DAT_010a14c0);
  FUN_00551e14(uVar1,param_2[0x3f],DAT_010a1420,param_2[0x41]);
  FUN_00551e14(uVar1,param_2[0x42],DAT_010a14e8);
  FUN_00551e14(uVar1,param_2[0x3f],DAT_010a1430,param_2[0x42]);
  _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv(uVar1,0,param_2 + 0x41);
  _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv(uVar1,0,param_2 + 0x42);
                    /* try { // try from 00b5e0b4 to 00c5e0d7 has its CatchHandler @ 00b5e58c */
  _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv(uVar1,0,param_2 + 0x40);
  _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv(uVar1,0,param_2 + 0x3f);
  if (DAT_010a14f8 == 0) {
    _ZN8firebase9LogAssertEPKcz("g_initialized_count");
  }
  DAT_010a14f8 = DAT_010a14f8 + -1;
  if (DAT_010a14f8 != 0) {
                    /* try { // try from 00b5e10c to 00c5e12f has its CatchHandler @ 00b5e588 */
    return;
  }
  _ZN8firebase4auth18ReleaseAuthClassesEP7_JNIEnv(uVar1);
  _ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv(uVar1);
  _ZN8firebase4auth24ReleaseCredentialClassesEP7_JNIEnv(uVar1);
  _ZN8firebase4auth20ReleaseCommonClassesEP7_JNIEnv(uVar1);
  _ZN8firebase4util9TerminateEP7_JNIEnv(uVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5dfec"></a> `00b5dfec` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00b5dff0"></a> `00b5dff0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5dff4"></a> `00b5dff4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5dff8"></a> `00b5dff8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5dffc"></a> `00b5dffc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b5e000"></a> `00b5e000` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-00b5e004"></a> `00b5e004` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b5e008"></a> `00b5e008` | `6a 00 02 94` | bl 0x00bde1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e00c"></a> `00b5e00c` | `88 02 45 39` | ldrb w8,[x20, #0x140] | `FALL_THROUGH`
<a id="insn-00b5e010"></a> `00b5e010` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b5e014"></a> `00b5e014` | `88 00 00 37` | tbnz w8,#0x0,0x00b5e024 | `CONDITIONAL_JUMP`
<a id="insn-00b5e018"></a> `00b5e018` | `88 02 05 91` | add x8,x20,#0x140 | `FALL_THROUGH`
<a id="insn-00b5e01c"></a> `00b5e01c` | `01 05 00 91` | add x1,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5e020"></a> `00b5e020` | `02 00 00 14` | b 0x00b5e028 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5e024"></a> `00b5e024` | `81 aa 40 f9` | ldr x1,[x20, #0x150] | `FALL_THROUGH`
<a id="insn-00b5e028"></a> `00b5e028` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e02c"></a> `00b5e02c` | `01 00 02 94` | bl 0x00bde030 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e030"></a> `00b5e030` | `08 2a 00 f0` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5e034"></a> `00b5e034` | `81 06 41 f9` | ldr x1,[x20, #0x208] | `FALL_THROUGH`
<a id="insn-00b5e038"></a> `00b5e038` | `02 61 42 f9` | ldr x2,[x8, #0x4c0] | `FALL_THROUGH`
<a id="insn-00b5e03c"></a> `00b5e03c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e040"></a> `00b5e040` | `95 22 08 91` | add x21,x20,#0x208 | `FALL_THROUGH`
<a id="insn-00b5e044"></a> `00b5e044` | `74 cf e7 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e048"></a> `00b5e048` | `18 2a 00 f0` | adrp x24,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5e04c"></a> `00b5e04c` | `18 83 10 91` | add x24,x24,#0x420 | `FALL_THROUGH`
<a id="insn-00b5e050"></a> `00b5e050` | `81 fe 40 f9` | ldr x1,[x20, #0x1f8] | `FALL_THROUGH`
<a id="insn-00b5e054"></a> `00b5e054` | `02 03 40 f9` | ldr x2,[x24] | `FALL_THROUGH`
<a id="insn-00b5e058"></a> `00b5e058` | `83 06 41 f9` | ldr x3,[x20, #0x208] | `FALL_THROUGH`
<a id="insn-00b5e05c"></a> `00b5e05c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e060"></a> `00b5e060` | `96 e2 07 91` | add x22,x20,#0x1f8 | `FALL_THROUGH`
<a id="insn-00b5e064"></a> `00b5e064` | `6c cf e7 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e068"></a> `00b5e068` | `08 2a 00 f0` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5e06c"></a> `00b5e06c` | `81 0a 41 f9` | ldr x1,[x20, #0x210] | `FALL_THROUGH`
<a id="insn-00b5e070"></a> `00b5e070` | `02 75 42 f9` | ldr x2,[x8, #0x4e8] | `FALL_THROUGH`
<a id="insn-00b5e074"></a> `00b5e074` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e078"></a> `00b5e078` | `97 42 08 91` | add x23,x20,#0x210 | `FALL_THROUGH`
<a id="insn-00b5e07c"></a> `00b5e07c` | `66 cf e7 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e080"></a> `00b5e080` | `81 fe 40 f9` | ldr x1,[x20, #0x1f8] | `FALL_THROUGH`
<a id="insn-00b5e084"></a> `00b5e084` | `02 0b 40 f9` | ldr x2,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b5e088"></a> `00b5e088` | `83 0a 41 f9` | ldr x3,[x20, #0x210] | `FALL_THROUGH`
<a id="insn-00b5e08c"></a> `00b5e08c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e090"></a> `00b5e090` | `61 cf e7 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e094"></a> `00b5e094` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e098"></a> `00b5e098` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b5e09c"></a> `00b5e09c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00b5e0a0"></a> `00b5e0a0` | `e4 0a 02 94` | bl 0x00be0c30 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e0a4"></a> `00b5e0a4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e0a8"></a> `00b5e0a8` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b5e0ac"></a> `00b5e0ac` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00b5e0b0"></a> `00b5e0b0` | `e0 0a 02 94` | bl 0x00be0c30 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e0b4"></a> `00b5e0b4` | `82 02 08 91` | add x2,x20,#0x200 | `FALL_THROUGH`
<a id="insn-00b5e0b8"></a> `00b5e0b8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e0bc"></a> `00b5e0bc` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b5e0c0"></a> `00b5e0c0` | `dc 0a 02 94` | bl 0x00be0c30 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e0c4"></a> `00b5e0c4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e0c8"></a> `00b5e0c8` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b5e0cc"></a> `00b5e0cc` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b5e0d0"></a> `00b5e0d0` | `d8 0a 02 94` | bl 0x00be0c30 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e0d4"></a> `00b5e0d4` | `14 2a 00 f0` | adrp x20,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5e0d8"></a> `00b5e0d8` | `88 fa 44 b9` | ldr w8,[x20, #0x4f8] | `FALL_THROUGH`
<a id="insn-00b5e0dc"></a> `00b5e0dc` | `a8 00 00 35` | cbnz w8,0x00b5e0f0 | `CONDITIONAL_JUMP`
<a id="insn-00b5e0e0"></a> `00b5e0e0` | `80 b9 ff f0` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00b5e0e4"></a> `00b5e0e4` | `00 f0 10 91` | add x0,x0,#0x43c | `FALL_THROUGH`
<a id="insn-00b5e0e8"></a> `00b5e0e8` | `12 00 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e0ec"></a> `00b5e0ec` | `88 fa 44 b9` | ldr w8,[x20, #0x4f8] | `FALL_THROUGH`
<a id="insn-00b5e0f0"></a> `00b5e0f0` | `08 05 00 71` | subs w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5e0f4"></a> `00b5e0f4` | `88 fa 04 b9` | str w8,[x20, #0x4f8] | `FALL_THROUGH`
<a id="insn-00b5e0f8"></a> `00b5e0f8` | `c0 00 00 54` | b.eq 0x00b5e110 | `CONDITIONAL_JUMP`
<a id="insn-00b5e0fc"></a> `00b5e0fc` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5e100"></a> `00b5e100` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5e104"></a> `00b5e104` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5e108"></a> `00b5e108` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b5e10c"></a> `00b5e10c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5e110"></a> `00b5e110` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e114"></a> `00b5e114` | `bf 0a 02 94` | bl 0x00be0c10 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e118"></a> `00b5e118` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e11c"></a> `00b5e11c` | `c1 0a 02 94` | bl 0x00be0c20 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e120"></a> `00b5e120` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e124"></a> `00b5e124` | `d3 0a 02 94` | bl 0x00be0c70 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e128"></a> `00b5e128` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e12c"></a> `00b5e12c` | `c9 0a 02 94` | bl 0x00be0c50 | `UNCONDITIONAL_CALL`
<a id="insn-00b5e130"></a> `00b5e130` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5e134"></a> `00b5e134` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5e138"></a> `00b5e138` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5e13c"></a> `00b5e13c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5e140"></a> `00b5e140` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b5e144"></a> `00b5e144` | `ef ff 01 14` | b 0x00bde100 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5dfec`](#insn-00b5dfec) 範囲 `[['00b5dfec', '00b5e017']]`
  - `CONDITIONAL_JUMP` [`00b5e014`](#insn-00b5e014) → [`00b5e024`](#insn-00b5e024)
  - `FALL_THROUGH` [`00b5e014`](#insn-00b5e014) → [`00b5e018`](#insn-00b5e018)
- ブロック [`00b5e018`](#insn-00b5e018) 範囲 `[['00b5e018', '00b5e023']]`
  - `UNCONDITIONAL_JUMP` [`00b5e020`](#insn-00b5e020) → [`00b5e028`](#insn-00b5e028)
- ブロック [`00b5e024`](#insn-00b5e024) 範囲 `[['00b5e024', '00b5e027']]`
  - `FALL_THROUGH` [`00b5e024`](#insn-00b5e024) → [`00b5e028`](#insn-00b5e028)
- ブロック [`00b5e028`](#insn-00b5e028) 範囲 `[['00b5e028', '00b5e043']]`
  - `FALL_THROUGH` [`00b5e040`](#insn-00b5e040) → [`00b5e044`](#insn-00b5e044)
- ブロック [`00b5e044`](#insn-00b5e044) 範囲 `[['00b5e044', '00b5e0b3']]`
  - `FALL_THROUGH` [`00b5e0b0`](#insn-00b5e0b0) → [`00b5e0b4`](#insn-00b5e0b4)
- ブロック [`00b5e0b4`](#insn-00b5e0b4) 範囲 `[['00b5e0b4', '00b5e0df']]`
  - `CONDITIONAL_JUMP` [`00b5e0dc`](#insn-00b5e0dc) → [`00b5e0f0`](#insn-00b5e0f0)
  - `FALL_THROUGH` [`00b5e0dc`](#insn-00b5e0dc) → [`00b5e0e0`](#insn-00b5e0e0)
- ブロック [`00b5e0e0`](#insn-00b5e0e0) 範囲 `[['00b5e0e0', '00b5e0ef']]`
  - `FALL_THROUGH` [`00b5e0ec`](#insn-00b5e0ec) → [`00b5e0f0`](#insn-00b5e0f0)
- ブロック [`00b5e0f0`](#insn-00b5e0f0) 範囲 `[['00b5e0f0', '00b5e0fb']]`
  - `CONDITIONAL_JUMP` [`00b5e0f8`](#insn-00b5e0f8) → [`00b5e110`](#insn-00b5e110)
  - `FALL_THROUGH` [`00b5e0f8`](#insn-00b5e0f8) → [`00b5e0fc`](#insn-00b5e0fc)
- ブロック [`00b5e0fc`](#insn-00b5e0fc) 範囲 `[['00b5e0fc', '00b5e10b']]`
  - `FALL_THROUGH` [`00b5e108`](#insn-00b5e108) → [`00b5e10c`](#insn-00b5e10c)
- ブロック [`00b5e10c`](#insn-00b5e10c) 範囲 `[['00b5e10c', '00b5e10f']]`
- ブロック [`00b5e110`](#insn-00b5e110) 範囲 `[['00b5e110', '00b5e147']]`

## 命令位置別の参照

- [`00b5dfec`](#insn-00b5dfec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5dff0`](#insn-00b5dff0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5dff4`](#insn-00b5dff4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5dff8`](#insn-00b5dff8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5e008`](#insn-00b5e008) → [`00bde1b0`](../00bde/00bde1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b5e014`](#insn-00b5e014) → [`00b5e024`](#insn-00b5e024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5e020`](#insn-00b5e020) → [`00b5e028`](#insn-00b5e028) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5e02c`](#insn-00b5e02c) → [`00bde030`](../00bde/00bde030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde030` · 推定シンボル `None` · 推定型 `None`
- [`00b5e038`](#insn-00b5e038) → `010a14c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5e044`](#insn-00b5e044) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00b5e054`](#insn-00b5e054) → `010a1420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5e064`](#insn-00b5e064) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00b5e070`](#insn-00b5e070) → `010a14e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5e07c`](#insn-00b5e07c) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00b5e084`](#insn-00b5e084) → `010a1430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5e090`](#insn-00b5e090) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00b5e0a0`](#insn-00b5e0a0) → [`00be0c30`](../00be0/00be0c30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0c30` · 推定シンボル `None` · 推定型 `None`
- [`00b5e0b0`](#insn-00b5e0b0) → [`00be0c30`](../00be0/00be0c30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0c30` · 推定シンボル `None` · 推定型 `None`
- [`00b5e0c0`](#insn-00b5e0c0) → [`00be0c30`](../00be0/00be0c30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0c30` · 推定シンボル `None` · 推定型 `None`
- [`00b5e0d0`](#insn-00b5e0d0) → [`00be0c30`](../00be0/00be0c30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0c30` · 推定シンボル `None` · 推定型 `None`
- [`00b5e0d8`](#insn-00b5e0d8) → `010a14f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00b5e0dc`](#insn-00b5e0dc) → [`00b5e0f0`](#insn-00b5e0f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5e0e4`](#insn-00b5e0e4) → `0029143c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b5e0e8`](#insn-00b5e0e8) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b5e0ec`](#insn-00b5e0ec) → `010a14f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00b5e0f4`](#insn-00b5e0f4) → `010a14f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00b5e0f8`](#insn-00b5e0f8) → [`00b5e110`](#insn-00b5e110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5e0fc`](#insn-00b5e0fc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5e100`](#insn-00b5e100) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5e104`](#insn-00b5e104) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5e114`](#insn-00b5e114) → [`00be0c10`](../00be0/00be0c10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0c10` · 推定シンボル `None` · 推定型 `None`
- [`00b5e11c`](#insn-00b5e11c) → [`00be0c20`](../00be0/00be0c20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0c20` · 推定シンボル `None` · 推定型 `None`
- [`00b5e124`](#insn-00b5e124) → [`00be0c70`](../00be0/00be0c70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0c70` · 推定シンボル `None` · 推定型 `None`
- [`00b5e12c`](#insn-00b5e12c) → [`00be0c50`](../00be0/00be0c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0c50` · 推定シンボル `None` · 推定型 `None`
- [`00b5e134`](#insn-00b5e134) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5e138`](#insn-00b5e138) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5e13c`](#insn-00b5e13c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5e144`](#insn-00b5e144) → [`00bde100`](../00bde/00bde100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde100` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5dfec`](#insn-00b5dfec)

~~~json
{
  "source": "00b5dfec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5dff0`](#insn-00b5dff0)

~~~json
{
  "source": "00b5dff0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5dff4`](#insn-00b5dff4)

~~~json
{
  "source": "00b5dff4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5dff8`](#insn-00b5dff8)

~~~json
{
  "source": "00b5dff8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5e008`](#insn-00b5e008)

~~~json
{
  "source": "00b5e008",
  "target": "00bde1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e014`](#insn-00b5e014)

~~~json
{
  "source": "00b5e014",
  "target": "00b5e024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5e020`](#insn-00b5e020)

~~~json
{
  "source": "00b5e020",
  "target": "00b5e028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5e02c`](#insn-00b5e02c)

~~~json
{
  "source": "00b5e02c",
  "target": "00bde030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e038`](#insn-00b5e038)

~~~json
{
  "source": "00b5e038",
  "target": "010a14c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a14c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5e044`](#insn-00b5e044)

~~~json
{
  "source": "00b5e044",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e054`](#insn-00b5e054)

~~~json
{
  "source": "00b5e054",
  "target": "010a1420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5e064`](#insn-00b5e064)

~~~json
{
  "source": "00b5e064",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e070`](#insn-00b5e070)

~~~json
{
  "source": "00b5e070",
  "target": "010a14e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a14e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5e07c`](#insn-00b5e07c)

~~~json
{
  "source": "00b5e07c",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e084`](#insn-00b5e084)

~~~json
{
  "source": "00b5e084",
  "target": "010a1430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1430",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5e090`](#insn-00b5e090)

~~~json
{
  "source": "00b5e090",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e0a0`](#insn-00b5e0a0)

~~~json
{
  "source": "00b5e0a0",
  "target": "00be0c30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e0b0`](#insn-00b5e0b0)

~~~json
{
  "source": "00b5e0b0",
  "target": "00be0c30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e0c0`](#insn-00b5e0c0)

~~~json
{
  "source": "00b5e0c0",
  "target": "00be0c30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e0d0`](#insn-00b5e0d0)

~~~json
{
  "source": "00b5e0d0",
  "target": "00be0c30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e0d8`](#insn-00b5e0d8)

~~~json
{
  "source": "00b5e0d8",
  "target": "010a14f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a14f8",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5e0dc`](#insn-00b5e0dc)

~~~json
{
  "source": "00b5e0dc",
  "target": "00b5e0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5e0e4`](#insn-00b5e0e4)

~~~json
{
  "source": "00b5e0e4",
  "target": "0029143c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029143c",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "675f696e697469616c697a65645f636f756e7400",
  "capture_start": "0029143c",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b5e0e8`](#insn-00b5e0e8)

~~~json
{
  "source": "00b5e0e8",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e0ec`](#insn-00b5e0ec)

~~~json
{
  "source": "00b5e0ec",
  "target": "010a14f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a14f8",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5e0f4`](#insn-00b5e0f4)

~~~json
{
  "source": "00b5e0f4",
  "target": "010a14f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a14f8",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5e0f8`](#insn-00b5e0f8)

~~~json
{
  "source": "00b5e0f8",
  "target": "00b5e110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5e0fc`](#insn-00b5e0fc)

~~~json
{
  "source": "00b5e0fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5e100`](#insn-00b5e100)

~~~json
{
  "source": "00b5e100",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5e104`](#insn-00b5e104)

~~~json
{
  "source": "00b5e104",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5e114`](#insn-00b5e114)

~~~json
{
  "source": "00b5e114",
  "target": "00be0c10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e11c`](#insn-00b5e11c)

~~~json
{
  "source": "00b5e11c",
  "target": "00be0c20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e124`](#insn-00b5e124)

~~~json
{
  "source": "00b5e124",
  "target": "00be0c70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e12c`](#insn-00b5e12c)

~~~json
{
  "source": "00b5e12c",
  "target": "00be0c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5e134`](#insn-00b5e134)

~~~json
{
  "source": "00b5e134",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5e138`](#insn-00b5e138)

~~~json
{
  "source": "00b5e138",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5e13c`](#insn-00b5e13c)

~~~json
{
  "source": "00b5e13c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5e144`](#insn-00b5e144)

~~~json
{
  "source": "00b5e144",
  "target": "00bde100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
