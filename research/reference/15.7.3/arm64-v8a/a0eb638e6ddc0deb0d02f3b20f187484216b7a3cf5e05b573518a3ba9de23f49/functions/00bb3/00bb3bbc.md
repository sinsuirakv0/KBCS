# 00bb3bbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bb3af4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb3/00bb3af4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0005.md#compare-bb6df1b56e6738f2910a2e365ede6a17)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bb3c00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb3/00bb3c00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0004.md#compare-d3c2f7e0ecf5842da5a88fbc4de80112)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb3bbc",
  "name": "_ZNSt6__ndk118__time_get_storageIcE4initERKNS_5ctypeIcEE",
  "size": 632,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "685e8e5874ce54aaece91e77b8086e452b27e99d9b8e5c0785b3e1273fe75362",
  "source_text_sha256": "685e8e5874ce54aaece91e77b8086e452b27e99d9b8e5c0785b3e1273fe75362",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb3bbc",
        "00bb3e33"
      ]
    ],
    "bytes_sha256": "c1c0032eca9cf0c3a250933eebf16ed1c33efee11b586ac6d805c56c292df748",
    "instruction_count": 158,
    "instruction_bytes": 632,
    "body_bytes": 632,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1cc0](../00be1/00be1cc0.md)

## 呼び出し先

- [00b750e4](../00b75/00b750e4.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00be1620](../00be1/00be1620.md)
- [00be1ca0](../00be1/00be1ca0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3449 bytes

~~~c

void _ZNSt6__ndk118__time_get_storageIcE4initERKNS_5ctypeIcEE
               (undefined8 *param_1,undefined8 param_2)

{
  undefined8 *puVar1;
  long lVar2;
  undefined8 local_100;
  undefined8 uStack_f8;
  undefined8 local_f0;
  char acStack_e4 [100];
  tm local_80;
  
  lVar2 = 0;
                    /* try { // try from 00bb3be8 to 00cb3bef has its CatchHandler @ 00bbac98 */
  puVar1 = param_1 + 0x16;
  local_80.tm_zone = (char *)0x0;
  local_80.tm_wday = 0;
  local_80.tm_yday = 0;
  local_80.tm_mon = 0;
  local_80.tm_year = 0;
  local_80.tm_gmtoff = 0;
  local_80.tm_isdst = 0;
  local_80._36_4_ = 0;
  local_80.tm_hour = 0;
  local_80.tm_mday = 0;
  local_80.tm_sec = 0;
  local_80.tm_min = 0;
  do {
    local_80.tm_wday = (int)lVar2;
    strftime_l(acStack_e4,100,"%A",&local_80,(__locale_t)*param_1);
    FUN_00b750e4(puVar1 + -0x15,acStack_e4);
    strftime_l(acStack_e4,100,"%a",&local_80,(__locale_t)*param_1);
    FUN_00b750e4(puVar1,acStack_e4);
    lVar2 = lVar2 + 1;
    puVar1 = puVar1 + 3;
  } while (lVar2 != 7);
  lVar2 = 0;
  puVar1 = param_1 + 0x4f;
  do {
    local_80.tm_mon = (int)lVar2;
    strftime_l(acStack_e4,100,"%B",&local_80,(__locale_t)*param_1);
    FUN_00b750e4(puVar1 + -0x24,acStack_e4);
    strftime_l(acStack_e4,100,"%b",&local_80,(__locale_t)*param_1);
    FUN_00b750e4(puVar1,acStack_e4);
    lVar2 = lVar2 + 1;
    puVar1 = puVar1 + 3;
                    /* try { // try from 00bb3cd0 to 00cb3cdb has its CatchHandler @ 00bbaa00 */
  } while (lVar2 != 0xc);
                    /* try { // try from 00bb3cdc to 00cb3ceb has its CatchHandler @ 00bba9ec */
                    /* try { // try from 00bb3cec to 00cb3cff has its CatchHandler @ 00bba9c0 */
  local_80.tm_hour = 1;
  strftime_l(acStack_e4,100,"%p",&local_80,(__locale_t)*param_1);
  FUN_00b750e4(param_1 + 0x73,acStack_e4);
  local_80.tm_hour = 0xd;
  strftime_l(acStack_e4,100,"%p",&local_80,(__locale_t)*param_1);
  FUN_00b750e4(param_1 + 0x76,acStack_e4);
  _ZNSt6__ndk118__time_get_storageIcE9__analyzeEcRKNS_5ctypeIcEE(&local_100,param_1,99,param_2);
  if ((*(byte *)(param_1 + 0x79) & 1) != 0) {
    _ZdlPv((void *)param_1[0x7b]);
  }
  param_1[0x7b] = local_f0;
  param_1[0x7a] = uStack_f8;
  param_1[0x79] = local_100;
  _ZNSt6__ndk118__time_get_storageIcE9__analyzeEcRKNS_5ctypeIcEE(&local_100,param_1,0x72,param_2);
  if ((*(byte *)(param_1 + 0x7c) & 1) != 0) {
    _ZdlPv((void *)param_1[0x7e]);
  }
                    /* try { // try from 00bb3dac to 00cb3dc3 has its CatchHandler @ 00bbaba0 */
  param_1[0x7e] = local_f0;
  param_1[0x7d] = uStack_f8;
  param_1[0x7c] = local_100;
  _ZNSt6__ndk118__time_get_storageIcE9__analyzeEcRKNS_5ctypeIcEE(&local_100,param_1,0x78,param_2);
  if ((*(byte *)(param_1 + 0x7f) & 1) != 0) {
    _ZdlPv((void *)param_1[0x81]);
  }
                    /* try { // try from 00bb3dd4 to 00cb3ddb has its CatchHandler @ 00bbad04 */
                    /* try { // try from 00bb3de4 to 00cb3df3 has its CatchHandler @ 00bbacf4 */
  param_1[0x81] = local_f0;
  param_1[0x80] = uStack_f8;
  param_1[0x7f] = local_100;
  _ZNSt6__ndk118__time_get_storageIcE9__analyzeEcRKNS_5ctypeIcEE(&local_100,param_1,0x58,param_2);
                    /* try { // try from 00bb3dfc to 00cb3e07 has its CatchHandler @ 00bbacf0 */
  if ((*(byte *)(param_1 + 0x82) & 1) != 0) {
    _ZdlPv((void *)param_1[0x84]);
  }
  param_1[0x83] = uStack_f8;
  param_1[0x82] = local_100;
  param_1[0x84] = local_f0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb3bbc"></a> `00bb3bbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bb3bc0"></a> `00bb3bc0` | `ff 03 04 d1` | sub sp,sp,#0x100 | `FALL_THROUGH`
<a id="insn-00bb3bc4"></a> `00bb3bc4` | `fd 7b 0c a9` | stp x29,x30,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bb3bc8"></a> `00bb3bc8` | `f8 5f 0d a9` | stp x24,x23,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bb3bcc"></a> `00bb3bcc` | `f6 57 0e a9` | stp x22,x21,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bb3bd0"></a> `00bb3bd0` | `f4 4f 0f a9` | stp x20,x19,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00bb3bd4"></a> `00bb3bd4` | `fd 03 03 91` | add x29,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00bb3bd8"></a> `00bb3bd8` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bb3bdc"></a> `00bb3bdc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bb3be0"></a> `00bb3be0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb3be4"></a> `00bb3be4` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00bb3be8"></a> `00bb3be8` | `75 b7 ff f0` | adrp x21,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bb3bec"></a> `00bb3bec` | `b5 d6 01 91` | add x21,x21,#0x75 | `FALL_THROUGH`
<a id="insn-00bb3bf0"></a> `00bb3bf0` | `16 c0 02 91` | add x22,x0,#0xb0 | `FALL_THROUGH`
<a id="insn-00bb3bf4"></a> `00bb3bf4` | `57 b7 ff b0` | adrp x23,0x29c000 | `FALL_THROUGH`
<a id="insn-00bb3bf8"></a> `00bb3bf8` | `f7 e6 0a 91` | add x23,x23,#0x2b9 | `FALL_THROUGH`
<a id="insn-00bb3bfc"></a> `00bb3bfc` | `bf 03 1f f8` | stur xzr,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bb3c00"></a> `00bb3c00` | `a0 83 3e ad` | stp q0,q0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00bb3c04"></a> `00bb3c04` | `a0 03 9c 3c` | stur q0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00bb3c08"></a> `00bb3c08` | `64 02 40 f9` | ldr x4,[x19] | `FALL_THROUGH`
<a id="insn-00bb3c0c"></a> `00bb3c0c` | `e0 73 00 91` | add x0,sp,#0x1c | `FALL_THROUGH`
<a id="insn-00bb3c10"></a> `00bb3c10` | `a3 03 01 d1` | sub x3,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00bb3c14"></a> `00bb3c14` | `81 0c 80 52` | mov w1,#0x64 | `FALL_THROUGH`
<a id="insn-00bb3c18"></a> `00bb3c18` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bb3c1c"></a> `00bb3c1c` | `b8 83 1d b8` | stur w24,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bb3c20"></a> `00bb3c20` | `80 b6 00 94` | bl 0x00be1620 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3c24"></a> `00bb3c24` | `c0 a2 02 d1` | sub x0,x22,#0xa8 | `FALL_THROUGH`
<a id="insn-00bb3c28"></a> `00bb3c28` | `e1 73 00 91` | add x1,sp,#0x1c | `FALL_THROUGH`
<a id="insn-00bb3c2c"></a> `00bb3c2c` | `2e 05 ff 97` | bl 0x00b750e4 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3c30"></a> `00bb3c30` | `64 02 40 f9` | ldr x4,[x19] | `FALL_THROUGH`
<a id="insn-00bb3c34"></a> `00bb3c34` | `e0 73 00 91` | add x0,sp,#0x1c | `FALL_THROUGH`
<a id="insn-00bb3c38"></a> `00bb3c38` | `a3 03 01 d1` | sub x3,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00bb3c3c"></a> `00bb3c3c` | `81 0c 80 52` | mov w1,#0x64 | `FALL_THROUGH`
<a id="insn-00bb3c40"></a> `00bb3c40` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00bb3c44"></a> `00bb3c44` | `77 b6 00 94` | bl 0x00be1620 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3c48"></a> `00bb3c48` | `e1 73 00 91` | add x1,sp,#0x1c | `FALL_THROUGH`
<a id="insn-00bb3c4c"></a> `00bb3c4c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bb3c50"></a> `00bb3c50` | `25 05 ff 97` | bl 0x00b750e4 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3c54"></a> `00bb3c54` | `18 07 00 91` | add x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bb3c58"></a> `00bb3c58` | `d6 62 00 91` | add x22,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00bb3c5c"></a> `00bb3c5c` | `1f 1f 00 f1` | cmp x24,#0x7 | `FALL_THROUGH`
<a id="insn-00bb3c60"></a> `00bb3c60` | `41 fd ff 54` | b.ne 0x00bb3c08 | `CONDITIONAL_JUMP`
<a id="insn-00bb3c64"></a> `00bb3c64` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00bb3c68"></a> `00bb3c68` | `75 b7 ff 90` | adrp x21,0x29f000 | `FALL_THROUGH`
<a id="insn-00bb3c6c"></a> `00bb3c6c` | `b5 a6 09 91` | add x21,x21,#0x269 | `FALL_THROUGH`
<a id="insn-00bb3c70"></a> `00bb3c70` | `76 e2 09 91` | add x22,x19,#0x278 | `FALL_THROUGH`
<a id="insn-00bb3c74"></a> `00bb3c74` | `17 b7 ff b0` | adrp x23,0x294000 | `FALL_THROUGH`
<a id="insn-00bb3c78"></a> `00bb3c78` | `f7 12 13 91` | add x23,x23,#0x4c4 | `FALL_THROUGH`
<a id="insn-00bb3c7c"></a> `00bb3c7c` | `64 02 40 f9` | ldr x4,[x19] | `FALL_THROUGH`
<a id="insn-00bb3c80"></a> `00bb3c80` | `e0 73 00 91` | add x0,sp,#0x1c | `FALL_THROUGH`
<a id="insn-00bb3c84"></a> `00bb3c84` | `a3 03 01 d1` | sub x3,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00bb3c88"></a> `00bb3c88` | `81 0c 80 52` | mov w1,#0x64 | `FALL_THROUGH`
<a id="insn-00bb3c8c"></a> `00bb3c8c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bb3c90"></a> `00bb3c90` | `b8 03 1d b8` | stur w24,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00bb3c94"></a> `00bb3c94` | `63 b6 00 94` | bl 0x00be1620 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3c98"></a> `00bb3c98` | `c0 82 04 d1` | sub x0,x22,#0x120 | `FALL_THROUGH`
<a id="insn-00bb3c9c"></a> `00bb3c9c` | `e1 73 00 91` | add x1,sp,#0x1c | `FALL_THROUGH`
<a id="insn-00bb3ca0"></a> `00bb3ca0` | `11 05 ff 97` | bl 0x00b750e4 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3ca4"></a> `00bb3ca4` | `64 02 40 f9` | ldr x4,[x19] | `FALL_THROUGH`
<a id="insn-00bb3ca8"></a> `00bb3ca8` | `e0 73 00 91` | add x0,sp,#0x1c | `FALL_THROUGH`
<a id="insn-00bb3cac"></a> `00bb3cac` | `a3 03 01 d1` | sub x3,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00bb3cb0"></a> `00bb3cb0` | `81 0c 80 52` | mov w1,#0x64 | `FALL_THROUGH`
<a id="insn-00bb3cb4"></a> `00bb3cb4` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00bb3cb8"></a> `00bb3cb8` | `5a b6 00 94` | bl 0x00be1620 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3cbc"></a> `00bb3cbc` | `e1 73 00 91` | add x1,sp,#0x1c | `FALL_THROUGH`
<a id="insn-00bb3cc0"></a> `00bb3cc0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bb3cc4"></a> `00bb3cc4` | `08 05 ff 97` | bl 0x00b750e4 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3cc8"></a> `00bb3cc8` | `18 07 00 91` | add x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bb3ccc"></a> `00bb3ccc` | `d6 62 00 91` | add x22,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00bb3cd0"></a> `00bb3cd0` | `1f 33 00 f1` | cmp x24,#0xc | `FALL_THROUGH`
<a id="insn-00bb3cd4"></a> `00bb3cd4` | `41 fd ff 54` | b.ne 0x00bb3c7c | `CONDITIONAL_JUMP`
<a id="insn-00bb3cd8"></a> `00bb3cd8` | `64 02 40 f9` | ldr x4,[x19] | `FALL_THROUGH`
<a id="insn-00bb3cdc"></a> `00bb3cdc` | `15 b7 ff f0` | adrp x21,0x296000 | `FALL_THROUGH`
<a id="insn-00bb3ce0"></a> `00bb3ce0` | `b5 de 1d 91` | add x21,x21,#0x777 | `FALL_THROUGH`
<a id="insn-00bb3ce4"></a> `00bb3ce4` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb3ce8"></a> `00bb3ce8` | `e0 73 00 91` | add x0,sp,#0x1c | `FALL_THROUGH`
<a id="insn-00bb3cec"></a> `00bb3cec` | `a3 03 01 d1` | sub x3,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00bb3cf0"></a> `00bb3cf0` | `81 0c 80 52` | mov w1,#0x64 | `FALL_THROUGH`
<a id="insn-00bb3cf4"></a> `00bb3cf4` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bb3cf8"></a> `00bb3cf8` | `a8 83 1c b8` | stur w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bb3cfc"></a> `00bb3cfc` | `49 b6 00 94` | bl 0x00be1620 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3d00"></a> `00bb3d00` | `60 62 0e 91` | add x0,x19,#0x398 | `FALL_THROUGH`
<a id="insn-00bb3d04"></a> `00bb3d04` | `e1 73 00 91` | add x1,sp,#0x1c | `FALL_THROUGH`
<a id="insn-00bb3d08"></a> `00bb3d08` | `f7 04 ff 97` | bl 0x00b750e4 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3d0c"></a> `00bb3d0c` | `64 02 40 f9` | ldr x4,[x19] | `FALL_THROUGH`
<a id="insn-00bb3d10"></a> `00bb3d10` | `a8 01 80 52` | mov w8,#0xd | `FALL_THROUGH`
<a id="insn-00bb3d14"></a> `00bb3d14` | `e0 73 00 91` | add x0,sp,#0x1c | `FALL_THROUGH`
<a id="insn-00bb3d18"></a> `00bb3d18` | `a3 03 01 d1` | sub x3,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00bb3d1c"></a> `00bb3d1c` | `81 0c 80 52` | mov w1,#0x64 | `FALL_THROUGH`
<a id="insn-00bb3d20"></a> `00bb3d20` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bb3d24"></a> `00bb3d24` | `a8 83 1c b8` | stur w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bb3d28"></a> `00bb3d28` | `3e b6 00 94` | bl 0x00be1620 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3d2c"></a> `00bb3d2c` | `60 c2 0e 91` | add x0,x19,#0x3b0 | `FALL_THROUGH`
<a id="insn-00bb3d30"></a> `00bb3d30` | `e1 73 00 91` | add x1,sp,#0x1c | `FALL_THROUGH`
<a id="insn-00bb3d34"></a> `00bb3d34` | `ec 04 ff 97` | bl 0x00b750e4 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3d38"></a> `00bb3d38` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bb3d3c"></a> `00bb3d3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb3d40"></a> `00bb3d40` | `61 0c 80 52` | mov w1,#0x63 | `FALL_THROUGH`
<a id="insn-00bb3d44"></a> `00bb3d44` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bb3d48"></a> `00bb3d48` | `d6 b7 00 94` | bl 0x00be1ca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3d4c"></a> `00bb3d4c` | `68 22 4f 39` | ldrb w8,[x19, #0x3c8] | `FALL_THROUGH`
<a id="insn-00bb3d50"></a> `00bb3d50` | `75 22 0f 91` | add x21,x19,#0x3c8 | `FALL_THROUGH`
<a id="insn-00bb3d54"></a> `00bb3d54` | `68 00 00 36` | tbz w8,#0x0,0x00bb3d60 | `CONDITIONAL_JUMP`
<a id="insn-00bb3d58"></a> `00bb3d58` | `60 ee 41 f9` | ldr x0,[x19, #0x3d8] | `FALL_THROUGH`
<a id="insn-00bb3d5c"></a> `00bb3d5c` | `ad 9c 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3d60"></a> `00bb3d60` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb3d64"></a> `00bb3d64` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bb3d68"></a> `00bb3d68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb3d6c"></a> `00bb3d6c` | `41 0e 80 52` | mov w1,#0x72 | `FALL_THROUGH`
<a id="insn-00bb3d70"></a> `00bb3d70` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bb3d74"></a> `00bb3d74` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bb3d78"></a> `00bb3d78` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bb3d7c"></a> `00bb3d7c` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00bb3d80"></a> `00bb3d80` | `c8 b7 00 94` | bl 0x00be1ca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3d84"></a> `00bb3d84` | `68 82 4f 39` | ldrb w8,[x19, #0x3e0] | `FALL_THROUGH`
<a id="insn-00bb3d88"></a> `00bb3d88` | `75 82 0f 91` | add x21,x19,#0x3e0 | `FALL_THROUGH`
<a id="insn-00bb3d8c"></a> `00bb3d8c` | `68 00 00 36` | tbz w8,#0x0,0x00bb3d98 | `CONDITIONAL_JUMP`
<a id="insn-00bb3d90"></a> `00bb3d90` | `60 fa 41 f9` | ldr x0,[x19, #0x3f0] | `FALL_THROUGH`
<a id="insn-00bb3d94"></a> `00bb3d94` | `9f 9c 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3d98"></a> `00bb3d98` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb3d9c"></a> `00bb3d9c` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bb3da0"></a> `00bb3da0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb3da4"></a> `00bb3da4` | `01 0f 80 52` | mov w1,#0x78 | `FALL_THROUGH`
<a id="insn-00bb3da8"></a> `00bb3da8` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bb3dac"></a> `00bb3dac` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bb3db0"></a> `00bb3db0` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bb3db4"></a> `00bb3db4` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00bb3db8"></a> `00bb3db8` | `ba b7 00 94` | bl 0x00be1ca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3dbc"></a> `00bb3dbc` | `68 e2 4f 39` | ldrb w8,[x19, #0x3f8] | `FALL_THROUGH`
<a id="insn-00bb3dc0"></a> `00bb3dc0` | `75 e2 0f 91` | add x21,x19,#0x3f8 | `FALL_THROUGH`
<a id="insn-00bb3dc4"></a> `00bb3dc4` | `68 00 00 36` | tbz w8,#0x0,0x00bb3dd0 | `CONDITIONAL_JUMP`
<a id="insn-00bb3dc8"></a> `00bb3dc8` | `60 06 42 f9` | ldr x0,[x19, #0x408] | `FALL_THROUGH`
<a id="insn-00bb3dcc"></a> `00bb3dcc` | `91 9c 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3dd0"></a> `00bb3dd0` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb3dd4"></a> `00bb3dd4` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bb3dd8"></a> `00bb3dd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb3ddc"></a> `00bb3ddc` | `01 0b 80 52` | mov w1,#0x58 | `FALL_THROUGH`
<a id="insn-00bb3de0"></a> `00bb3de0` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bb3de4"></a> `00bb3de4` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bb3de8"></a> `00bb3de8` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bb3dec"></a> `00bb3dec` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00bb3df0"></a> `00bb3df0` | `ac b7 00 94` | bl 0x00be1ca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3df4"></a> `00bb3df4` | `68 42 50 39` | ldrb w8,[x19, #0x410] | `FALL_THROUGH`
<a id="insn-00bb3df8"></a> `00bb3df8` | `74 42 10 91` | add x20,x19,#0x410 | `FALL_THROUGH`
<a id="insn-00bb3dfc"></a> `00bb3dfc` | `68 00 00 36` | tbz w8,#0x0,0x00bb3e08 | `CONDITIONAL_JUMP`
<a id="insn-00bb3e00"></a> `00bb3e00` | `60 12 42 f9` | ldr x0,[x19, #0x420] | `FALL_THROUGH`
<a id="insn-00bb3e04"></a> `00bb3e04` | `83 9c 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb3e08"></a> `00bb3e08` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bb3e0c"></a> `00bb3e0c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb3e10"></a> `00bb3e10` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00bb3e14"></a> `00bb3e14` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bb3e18"></a> `00bb3e18` | `f4 4f 4f a9` | ldp x20,x19,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00bb3e1c"></a> `00bb3e1c` | `f6 57 4e a9` | ldp x22,x21,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bb3e20"></a> `00bb3e20` | `f8 5f 4d a9` | ldp x24,x23,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bb3e24"></a> `00bb3e24` | `fd 7b 4c a9` | ldp x29,x30,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bb3e28"></a> `00bb3e28` | `ff 03 04 91` | add sp,sp,#0x100 | `FALL_THROUGH`
<a id="insn-00bb3e2c"></a> `00bb3e2c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb3e30"></a> `00bb3e30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb3bbc`](#insn-00bb3bbc) 範囲 `[['00bb3bbc', '00bb3be7']]`
  - `FALL_THROUGH` [`00bb3be4`](#insn-00bb3be4) → [`00bb3be8`](#insn-00bb3be8)
- ブロック [`00bb3be8`](#insn-00bb3be8) 範囲 `[['00bb3be8', '00bb3c07']]`
  - `FALL_THROUGH` [`00bb3c04`](#insn-00bb3c04) → [`00bb3c08`](#insn-00bb3c08)
- ブロック [`00bb3c08`](#insn-00bb3c08) 範囲 `[['00bb3c08', '00bb3c63']]`
  - `CONDITIONAL_JUMP` [`00bb3c60`](#insn-00bb3c60) → [`00bb3c08`](#insn-00bb3c08)
  - `FALL_THROUGH` [`00bb3c60`](#insn-00bb3c60) → [`00bb3c64`](#insn-00bb3c64)
- ブロック [`00bb3c64`](#insn-00bb3c64) 範囲 `[['00bb3c64', '00bb3c7b']]`
  - `FALL_THROUGH` [`00bb3c78`](#insn-00bb3c78) → [`00bb3c7c`](#insn-00bb3c7c)
- ブロック [`00bb3c7c`](#insn-00bb3c7c) 範囲 `[['00bb3c7c', '00bb3ccf']]`
  - `FALL_THROUGH` [`00bb3ccc`](#insn-00bb3ccc) → [`00bb3cd0`](#insn-00bb3cd0)
- ブロック [`00bb3cd0`](#insn-00bb3cd0) 範囲 `[['00bb3cd0', '00bb3cd7']]`
  - `CONDITIONAL_JUMP` [`00bb3cd4`](#insn-00bb3cd4) → [`00bb3c7c`](#insn-00bb3c7c)
  - `FALL_THROUGH` [`00bb3cd4`](#insn-00bb3cd4) → [`00bb3cd8`](#insn-00bb3cd8)
- ブロック [`00bb3cd8`](#insn-00bb3cd8) 範囲 `[['00bb3cd8', '00bb3cdb']]`
  - `FALL_THROUGH` [`00bb3cd8`](#insn-00bb3cd8) → [`00bb3cdc`](#insn-00bb3cdc)
- ブロック [`00bb3cdc`](#insn-00bb3cdc) 範囲 `[['00bb3cdc', '00bb3ceb']]`
  - `FALL_THROUGH` [`00bb3ce8`](#insn-00bb3ce8) → [`00bb3cec`](#insn-00bb3cec)
- ブロック [`00bb3cec`](#insn-00bb3cec) 範囲 `[['00bb3cec', '00bb3d57']]`
  - `CONDITIONAL_JUMP` [`00bb3d54`](#insn-00bb3d54) → [`00bb3d60`](#insn-00bb3d60)
  - `FALL_THROUGH` [`00bb3d54`](#insn-00bb3d54) → [`00bb3d58`](#insn-00bb3d58)
- ブロック [`00bb3d58`](#insn-00bb3d58) 範囲 `[['00bb3d58', '00bb3d5f']]`
  - `FALL_THROUGH` [`00bb3d5c`](#insn-00bb3d5c) → [`00bb3d60`](#insn-00bb3d60)
- ブロック [`00bb3d60`](#insn-00bb3d60) 範囲 `[['00bb3d60', '00bb3d8f']]`
  - `CONDITIONAL_JUMP` [`00bb3d8c`](#insn-00bb3d8c) → [`00bb3d98`](#insn-00bb3d98)
  - `FALL_THROUGH` [`00bb3d8c`](#insn-00bb3d8c) → [`00bb3d90`](#insn-00bb3d90)
- ブロック [`00bb3d90`](#insn-00bb3d90) 範囲 `[['00bb3d90', '00bb3d97']]`
  - `FALL_THROUGH` [`00bb3d94`](#insn-00bb3d94) → [`00bb3d98`](#insn-00bb3d98)
- ブロック [`00bb3d98`](#insn-00bb3d98) 範囲 `[['00bb3d98', '00bb3dab']]`
  - `FALL_THROUGH` [`00bb3da8`](#insn-00bb3da8) → [`00bb3dac`](#insn-00bb3dac)
- ブロック [`00bb3dac`](#insn-00bb3dac) 範囲 `[['00bb3dac', '00bb3dc7']]`
  - `CONDITIONAL_JUMP` [`00bb3dc4`](#insn-00bb3dc4) → [`00bb3dd0`](#insn-00bb3dd0)
  - `FALL_THROUGH` [`00bb3dc4`](#insn-00bb3dc4) → [`00bb3dc8`](#insn-00bb3dc8)
- ブロック [`00bb3dc8`](#insn-00bb3dc8) 範囲 `[['00bb3dc8', '00bb3dcf']]`
  - `FALL_THROUGH` [`00bb3dcc`](#insn-00bb3dcc) → [`00bb3dd0`](#insn-00bb3dd0)
- ブロック [`00bb3dd0`](#insn-00bb3dd0) 範囲 `[['00bb3dd0', '00bb3dd3']]`
  - `FALL_THROUGH` [`00bb3dd0`](#insn-00bb3dd0) → [`00bb3dd4`](#insn-00bb3dd4)
- ブロック [`00bb3dd4`](#insn-00bb3dd4) 範囲 `[['00bb3dd4', '00bb3de3']]`
  - `FALL_THROUGH` [`00bb3de0`](#insn-00bb3de0) → [`00bb3de4`](#insn-00bb3de4)
- ブロック [`00bb3de4`](#insn-00bb3de4) 範囲 `[['00bb3de4', '00bb3dfb']]`
  - `FALL_THROUGH` [`00bb3df8`](#insn-00bb3df8) → [`00bb3dfc`](#insn-00bb3dfc)
- ブロック [`00bb3dfc`](#insn-00bb3dfc) 範囲 `[['00bb3dfc', '00bb3dff']]`
  - `CONDITIONAL_JUMP` [`00bb3dfc`](#insn-00bb3dfc) → [`00bb3e08`](#insn-00bb3e08)
  - `FALL_THROUGH` [`00bb3dfc`](#insn-00bb3dfc) → [`00bb3e00`](#insn-00bb3e00)
- ブロック [`00bb3e00`](#insn-00bb3e00) 範囲 `[['00bb3e00', '00bb3e07']]`
  - `FALL_THROUGH` [`00bb3e04`](#insn-00bb3e04) → [`00bb3e08`](#insn-00bb3e08)
- ブロック [`00bb3e08`](#insn-00bb3e08) 範囲 `[['00bb3e08', '00bb3e33']]`

## 命令位置別の参照

- [`00bb3bc4`](#insn-00bb3bc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3bc8`](#insn-00bb3bc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3bcc`](#insn-00bb3bcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3bd0`](#insn-00bb3bd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3bfc`](#insn-00bb3bfc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c00`](#insn-00bb3c00) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c04`](#insn-00bb3c04) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c18`](#insn-00bb3c18) → `002a2075`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c1c`](#insn-00bb3c1c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c20`](#insn-00bb3c20) → [`00be1620`](../00be1/00be1620.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1620` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c2c`](#insn-00bb3c2c) → [`00b750e4`](../00b75/00b750e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b750e4` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c40`](#insn-00bb3c40) → `0029c2b9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c44`](#insn-00bb3c44) → [`00be1620`](../00be1/00be1620.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1620` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c50`](#insn-00bb3c50) → [`00b750e4`](../00b75/00b750e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b750e4` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c60`](#insn-00bb3c60) → [`00bb3c08`](#insn-00bb3c08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c8c`](#insn-00bb3c8c) → `0029f269`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c90`](#insn-00bb3c90) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3c94`](#insn-00bb3c94) → [`00be1620`](../00be1/00be1620.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1620` · 推定シンボル `None` · 推定型 `None`
- [`00bb3ca0`](#insn-00bb3ca0) → [`00b750e4`](../00b75/00b750e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b750e4` · 推定シンボル `None` · 推定型 `None`
- [`00bb3cb4`](#insn-00bb3cb4) → `002944c4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3cb8`](#insn-00bb3cb8) → [`00be1620`](../00be1/00be1620.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1620` · 推定シンボル `None` · 推定型 `None`
- [`00bb3cc4`](#insn-00bb3cc4) → [`00b750e4`](../00b75/00b750e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b750e4` · 推定シンボル `None` · 推定型 `None`
- [`00bb3cd4`](#insn-00bb3cd4) → [`00bb3c7c`](#insn-00bb3c7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3cf4`](#insn-00bb3cf4) → `00296777`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3cf8`](#insn-00bb3cf8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3cfc`](#insn-00bb3cfc) → [`00be1620`](../00be1/00be1620.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1620` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d08`](#insn-00bb3d08) → [`00b750e4`](../00b75/00b750e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b750e4` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d20`](#insn-00bb3d20) → `00296777`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d24`](#insn-00bb3d24) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d28`](#insn-00bb3d28) → [`00be1620`](../00be1/00be1620.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1620` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d34`](#insn-00bb3d34) → [`00b750e4`](../00b75/00b750e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b750e4` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d48`](#insn-00bb3d48) → [`00be1ca0`](../00be1/00be1ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1ca0` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d54`](#insn-00bb3d54) → [`00bb3d60`](#insn-00bb3d60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d5c`](#insn-00bb3d5c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d60`](#insn-00bb3d60) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d64`](#insn-00bb3d64) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d80`](#insn-00bb3d80) → [`00be1ca0`](../00be1/00be1ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1ca0` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d8c`](#insn-00bb3d8c) → [`00bb3d98`](#insn-00bb3d98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d94`](#insn-00bb3d94) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d98`](#insn-00bb3d98) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3d9c`](#insn-00bb3d9c) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3db8`](#insn-00bb3db8) → [`00be1ca0`](../00be1/00be1ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1ca0` · 推定シンボル `None` · 推定型 `None`
- [`00bb3dc4`](#insn-00bb3dc4) → [`00bb3dd0`](#insn-00bb3dd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3dcc`](#insn-00bb3dcc) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb3dd0`](#insn-00bb3dd0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3dd4`](#insn-00bb3dd4) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3df0`](#insn-00bb3df0) → [`00be1ca0`](../00be1/00be1ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1ca0` · 推定シンボル `None` · 推定型 `None`
- [`00bb3dfc`](#insn-00bb3dfc) → [`00bb3e08`](#insn-00bb3e08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3e04`](#insn-00bb3e04) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb3e08`](#insn-00bb3e08) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3e0c`](#insn-00bb3e0c) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3e18`](#insn-00bb3e18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3e1c`](#insn-00bb3e1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3e20`](#insn-00bb3e20) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3e24`](#insn-00bb3e24) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb3bc4`](#insn-00bb3bc4)

~~~json
{
  "source": "00bb3bc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3bc8`](#insn-00bb3bc8)

~~~json
{
  "source": "00bb3bc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3bcc`](#insn-00bb3bcc)

~~~json
{
  "source": "00bb3bcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3bd0`](#insn-00bb3bd0)

~~~json
{
  "source": "00bb3bd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3bfc`](#insn-00bb3bfc)

~~~json
{
  "source": "00bb3bfc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3c00`](#insn-00bb3c00)

~~~json
{
  "source": "00bb3c00",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3c04`](#insn-00bb3c04)

~~~json
{
  "source": "00bb3c04",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3c18`](#insn-00bb3c18)

~~~json
{
  "source": "00bb3c18",
  "target": "002a2075",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3c1c`](#insn-00bb3c1c)

~~~json
{
  "source": "00bb3c1c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3c20`](#insn-00bb3c20)

~~~json
{
  "source": "00bb3c20",
  "target": "00be1620",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3c2c`](#insn-00bb3c2c)

~~~json
{
  "source": "00bb3c2c",
  "target": "00b750e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3c40`](#insn-00bb3c40)

~~~json
{
  "source": "00bb3c40",
  "target": "0029c2b9",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3c44`](#insn-00bb3c44)

~~~json
{
  "source": "00bb3c44",
  "target": "00be1620",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3c50`](#insn-00bb3c50)

~~~json
{
  "source": "00bb3c50",
  "target": "00b750e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3c60`](#insn-00bb3c60)

~~~json
{
  "source": "00bb3c60",
  "target": "00bb3c08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3c8c`](#insn-00bb3c8c)

~~~json
{
  "source": "00bb3c8c",
  "target": "0029f269",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3c90`](#insn-00bb3c90)

~~~json
{
  "source": "00bb3c90",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3c94`](#insn-00bb3c94)

~~~json
{
  "source": "00bb3c94",
  "target": "00be1620",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3ca0`](#insn-00bb3ca0)

~~~json
{
  "source": "00bb3ca0",
  "target": "00b750e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3cb4`](#insn-00bb3cb4)

~~~json
{
  "source": "00bb3cb4",
  "target": "002944c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3cb8`](#insn-00bb3cb8)

~~~json
{
  "source": "00bb3cb8",
  "target": "00be1620",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3cc4`](#insn-00bb3cc4)

~~~json
{
  "source": "00bb3cc4",
  "target": "00b750e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3cd4`](#insn-00bb3cd4)

~~~json
{
  "source": "00bb3cd4",
  "target": "00bb3c7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3cf4`](#insn-00bb3cf4)

~~~json
{
  "source": "00bb3cf4",
  "target": "00296777",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3cf8`](#insn-00bb3cf8)

~~~json
{
  "source": "00bb3cf8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3cfc`](#insn-00bb3cfc)

~~~json
{
  "source": "00bb3cfc",
  "target": "00be1620",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3d08`](#insn-00bb3d08)

~~~json
{
  "source": "00bb3d08",
  "target": "00b750e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3d20`](#insn-00bb3d20)

~~~json
{
  "source": "00bb3d20",
  "target": "00296777",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3d24`](#insn-00bb3d24)

~~~json
{
  "source": "00bb3d24",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3d28`](#insn-00bb3d28)

~~~json
{
  "source": "00bb3d28",
  "target": "00be1620",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3d34`](#insn-00bb3d34)

~~~json
{
  "source": "00bb3d34",
  "target": "00b750e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3d48`](#insn-00bb3d48)

~~~json
{
  "source": "00bb3d48",
  "target": "00be1ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3d54`](#insn-00bb3d54)

~~~json
{
  "source": "00bb3d54",
  "target": "00bb3d60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3d5c`](#insn-00bb3d5c)

~~~json
{
  "source": "00bb3d5c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3d60`](#insn-00bb3d60)

~~~json
{
  "source": "00bb3d60",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3d64`](#insn-00bb3d64)

~~~json
{
  "source": "00bb3d64",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3d80`](#insn-00bb3d80)

~~~json
{
  "source": "00bb3d80",
  "target": "00be1ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3d8c`](#insn-00bb3d8c)

~~~json
{
  "source": "00bb3d8c",
  "target": "00bb3d98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3d94`](#insn-00bb3d94)

~~~json
{
  "source": "00bb3d94",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3d98`](#insn-00bb3d98)

~~~json
{
  "source": "00bb3d98",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3d9c`](#insn-00bb3d9c)

~~~json
{
  "source": "00bb3d9c",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3db8`](#insn-00bb3db8)

~~~json
{
  "source": "00bb3db8",
  "target": "00be1ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3dc4`](#insn-00bb3dc4)

~~~json
{
  "source": "00bb3dc4",
  "target": "00bb3dd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3dcc`](#insn-00bb3dcc)

~~~json
{
  "source": "00bb3dcc",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3dd0`](#insn-00bb3dd0)

~~~json
{
  "source": "00bb3dd0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3dd4`](#insn-00bb3dd4)

~~~json
{
  "source": "00bb3dd4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3df0`](#insn-00bb3df0)

~~~json
{
  "source": "00bb3df0",
  "target": "00be1ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3dfc`](#insn-00bb3dfc)

~~~json
{
  "source": "00bb3dfc",
  "target": "00bb3e08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3e04`](#insn-00bb3e04)

~~~json
{
  "source": "00bb3e04",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3e08`](#insn-00bb3e08)

~~~json
{
  "source": "00bb3e08",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3e0c`](#insn-00bb3e0c)

~~~json
{
  "source": "00bb3e0c",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3e18`](#insn-00bb3e18)

~~~json
{
  "source": "00bb3e18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3e1c`](#insn-00bb3e1c)

~~~json
{
  "source": "00bb3e1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3e20`](#insn-00bb3e20)

~~~json
{
  "source": "00bb3e20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3e24`](#insn-00bb3e24)

~~~json
{
  "source": "00bb3e24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
