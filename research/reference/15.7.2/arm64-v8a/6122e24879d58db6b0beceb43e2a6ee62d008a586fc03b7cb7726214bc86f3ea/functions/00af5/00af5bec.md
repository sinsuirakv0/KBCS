# 00af5bec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00af5cb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5cb4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-293dbdef66039b6c1c8c6b6fdfa34841)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af5bec",
  "name": "_ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afa9c1d15e8a8d8b7216e84dad9482c837aaa477259a8aafd19f3928f249dd0e",
  "source_text_sha256": "afa9c1d15e8a8d8b7216e84dad9482c837aaa477259a8aafd19f3928f249dd0e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af5bec",
        "00af5df3"
      ]
    ],
    "bytes_sha256": "44ca1fd4b916931063724da4fbd5b068e17f3c5f4bd1e7a4a88c6eea2d324a4f",
    "instruction_count": 130,
    "instruction_bytes": 520,
    "body_bytes": 520,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00bddfc0](../00bdd/00bddfc0.md)

## 呼び出し先

- [0056681c](../00566/0056681c.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bde660](../00bde/00bde660.md)
- [00bde720](../00bde/00bde720.md)
- [00bde730](../00bde/00bde730.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5215 bytes

~~~c

void _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
               (long *param_1,undefined8 param_2,undefined8 param_3,long param_4,ulong param_5)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  undefined8 *puVar4;
  long lVar5;
  undefined8 *puVar6;
  long *plVar7;
  long *plVar8;
  long *plVar9;
  long *plVar10;
  
                    /* try { // try from 00af5bec to 00bf5bf3 has its CatchHandler @ 00affc2c */
                    /* try { // try from 00af5bf8 to 00bf5bff has its CatchHandler @ 00affc20 */
                    /* try { // try from 00af5c04 to 00bf5c0b has its CatchHandler @ 00affc08 */
                    /* try { // try from 00af5c10 to 00bf5c17 has its CatchHandler @ 00affbfc */
                    /* try { // try from 00af5c1c to 00bf5c23 has its CatchHandler @ 00affbe4 */
  pthread_mutex_lock((pthread_mutex_t *)&DAT_010a09c8);
  plVar7 = DAT_010a09c0;
  plVar8 = DAT_010a09c0 + 1;
                    /* try { // try from 00af5c28 to 00bf5c2f has its CatchHandler @ 00affbd8 */
                    /* try { // try from 00af5c34 to 00bf5c3b has its CatchHandler @ 00affbc0 */
  plVar9 = (long *)*plVar8;
  plVar2 = plVar8;
  if (plVar9 == (long *)0x0) {
LAB_00af5c7c:
    puVar6 = (undefined8 *)*plVar8;
    plVar10 = plVar8;
  }
  else {
    plVar8 = DAT_010a09c0 + 1;
    do {
      while (plVar10 = plVar9, plVar2 = plVar10, (ulong)plVar10[4] <= param_5) {
        if (param_5 <= (ulong)plVar10[4]) goto LAB_00af5c7c;
        plVar8 = plVar10 + 1;
        plVar9 = (long *)*plVar8;
        if ((long *)*plVar8 == (long *)0x0) goto LAB_00af5c7c;
      }
      plVar8 = plVar10;
      plVar9 = (long *)*plVar10;
    } while ((long *)*plVar10 != (long *)0x0);
    puVar6 = (undefined8 *)*plVar10;
                    /* try { // try from 00af5cc8 to 00bf5ccf has its CatchHandler @ 00affb6c */
  }
                    /* try { // try from 00af5c80 to 00bf5c87 has its CatchHandler @ 00affbb4 */
  if (puVar6 == (undefined8 *)0x0) {
    puVar6 = (undefined8 *)_Znwm(0x40);
                    /* try { // try from 00af5c8c to 00bf5c93 has its CatchHandler @ 00affba8 */
    *puVar6 = 0;
    puVar6[1] = 0;
    puVar6[2] = plVar2;
                    /* try { // try from 00af5c98 to 00bf5c9f has its CatchHandler @ 00affb9c */
    puVar6[4] = param_5;
    puVar6[5] = puVar6 + 5;
    puVar6[6] = puVar6 + 5;
    puVar6[7] = 0;
    *plVar10 = (long)puVar6;
                    /* try { // try from 00af5ca4 to 00bf5cab has its CatchHandler @ 00affb90 */
                    /* try { // try from 00af5cb0 to 00bf5cb7 has its CatchHandler @ 00affb84 */
    puVar4 = puVar6;
    if (*(long *)*plVar7 != 0) {
      *plVar7 = *(long *)*plVar7;
      puVar4 = (undefined8 *)*plVar10;
                    /* try { // try from 00af5cbc to 00bf5cc3 has its CatchHandler @ 00affb78 */
    }
                    /* try { // try from 00af5cd4 to 00bf5cdb has its CatchHandler @ 00affb54 */
    _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_(plVar7[1],puVar4);
                    /* try { // try from 00af5ce0 to 00bf5ce7 has its CatchHandler @ 00affb48 */
    plVar7[2] = plVar7[2] + 1;
  }
                    /* try { // try from 00af5cec to 00bf5cf3 has its CatchHandler @ 00affb30 */
  plVar2 = (long *)_Znwm(0x38);
  plVar2[5] = 0;
  plVar2[6] = 0;
                    /* try { // try from 00af5cf8 to 00bf5cff has its CatchHandler @ 00affb28 */
  plVar2[4] = 0;
  plVar2[1] = (long)(puVar6 + 5);
  lVar5 = puVar6[5];
                    /* try { // try from 00af5d04 to 00bf5d17 has its CatchHandler @ 00afffd8 */
  *plVar2 = lVar5;
  *(long **)(lVar5 + 8) = plVar2;
  puVar6[5] = plVar2;
                    /* try { // try from 00af5d20 to 00bf5d27 has its CatchHandler @ 00affb20 */
  puVar6[7] = puVar6[7] + 1;
  plVar7 = plVar2 + 2;
  *plVar7 = 0;
  plVar2[3] = param_4;
  plVar2[4] = (long)plVar2;
                    /* try { // try from 00af5d2c to 00bf5d3f has its CatchHandler @ 00afff94 */
  plVar2[5] = (long)(puVar6 + 5);
  *(undefined1 *)(plVar2 + 6) = 0;
                    /* try { // try from 00af5d40 to 00bf5d5b has its CatchHandler @ 00af560c */
  pthread_mutex_unlock((pthread_mutex_t *)&DAT_010a09c8);
                    /* try { // try from 00af5d5c to 00bf5d63 has its CatchHandler @ 00affb18 */
                    /* try { // try from 00af5d64 to 00bf5ee7 has its CatchHandler @ 00af560c */
  uVar3 = FUN_0056681c(param_1,DAT_010a0290,DAT_010a02a0,param_2,param_3,plVar7);
  pthread_mutex_lock((pthread_mutex_t *)&DAT_010a09c8);
  if ((char)plVar2[6] == '\0') {
    lVar5 = (**(code **)(*param_1 + 0xa8))(param_1,uVar3);
    *plVar7 = lVar5;
  }
  else {
    plVar7 = (long *)plVar2[4];
    lVar1 = plVar2[5];
    lVar5 = *plVar7;
    *(long *)(lVar5 + 8) = plVar7[1];
    *(long *)plVar7[1] = lVar5;
    *(long *)(lVar1 + 0x10) = *(long *)(lVar1 + 0x10) + -1;
    _ZdlPv(plVar7);
  }
  pthread_mutex_unlock((pthread_mutex_t *)&DAT_010a09c8);
                    /* WARNING: Could not recover jumptable at 0x00af5df0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_1 + 0xb8))(param_1,uVar3);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af5bec"></a> `00af5bec` | `fb 0f 1a f8` | str x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00af5bf0"></a> `00af5bf0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af5bf4"></a> `00af5bf4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af5bf8"></a> `00af5bf8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af5bfc"></a> `00af5bfc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00af5c00"></a> `00af5c00` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00af5c04"></a> `00af5c04` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00af5c08"></a> `00af5c08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af5c0c"></a> `00af5c0c` | `40 2d 00 f0` | adrp x0,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af5c10"></a> `00af5c10` | `00 20 27 91` | add x0,x0,#0x9c8 | `FALL_THROUGH`
<a id="insn-00af5c14"></a> `00af5c14` | `f7 03 04 aa` | mov x23,x4 | `FALL_THROUGH`
<a id="insn-00af5c18"></a> `00af5c18` | `f6 03 03 aa` | mov x22,x3 | `FALL_THROUGH`
<a id="insn-00af5c1c"></a> `00af5c1c` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00af5c20"></a> `00af5c20` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00af5c24"></a> `00af5c24` | `bf a2 03 94` | bl 0x00bde720 | `UNCONDITIONAL_CALL`
<a id="insn-00af5c28"></a> `00af5c28` | `48 2d 00 f0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af5c2c"></a> `00af5c2c` | `19 e1 44 f9` | ldr x25,[x8, #0x9c0] | `FALL_THROUGH`
<a id="insn-00af5c30"></a> `00af5c30` | `fa 03 19 aa` | mov x26,x25 | `FALL_THROUGH`
<a id="insn-00af5c34"></a> `00af5c34` | `5b 8f 40 f8` | ldr x27,[x26, #0x8]! | `FALL_THROUGH`
<a id="insn-00af5c38"></a> `00af5c38` | `1b 02 00 b4` | cbz x27,0x00af5c78 | `CONDITIONAL_JUMP`
<a id="insn-00af5c3c"></a> `00af5c3c` | `3a 23 00 91` | add x26,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00af5c40"></a> `00af5c40` | `68 13 40 f9` | ldr x8,[x27, #0x20] | `FALL_THROUGH`
<a id="insn-00af5c44"></a> `00af5c44` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00af5c48"></a> `00af5c48` | `c9 00 00 54` | b.ls 0x00af5c60 | `CONDITIONAL_JUMP`
<a id="insn-00af5c4c"></a> `00af5c4c` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00af5c50"></a> `00af5c50` | `88 03 00 b4` | cbz x8,0x00af5cc0 | `CONDITIONAL_JUMP`
<a id="insn-00af5c54"></a> `00af5c54` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00af5c58"></a> `00af5c58` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00af5c5c"></a> `00af5c5c` | `f9 ff ff 17` | b 0x00af5c40 | `UNCONDITIONAL_JUMP`
<a id="insn-00af5c60"></a> `00af5c60` | `e2 00 00 54` | b.cs 0x00af5c7c | `CONDITIONAL_JUMP`
<a id="insn-00af5c64"></a> `00af5c64` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00af5c68"></a> `00af5c68` | `48 8f 40 f8` | ldr x8,[x26, #0x8]! | `FALL_THROUGH`
<a id="insn-00af5c6c"></a> `00af5c6c` | `88 00 00 b4` | cbz x8,0x00af5c7c | `CONDITIONAL_JUMP`
<a id="insn-00af5c70"></a> `00af5c70` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00af5c74"></a> `00af5c74` | `f3 ff ff 17` | b 0x00af5c40 | `UNCONDITIONAL_JUMP`
<a id="insn-00af5c78"></a> `00af5c78` | `fb 03 1a aa` | mov x27,x26 | `FALL_THROUGH`
<a id="insn-00af5c7c"></a> `00af5c7c` | `58 03 40 f9` | ldr x24,[x26] | `FALL_THROUGH`
<a id="insn-00af5c80"></a> `00af5c80` | `58 03 00 b5` | cbnz x24,0x00af5ce8 | `CONDITIONAL_JUMP`
<a id="insn-00af5c84"></a> `00af5c84` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00af5c88"></a> `00af5c88` | `ae 94 03 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00af5c8c"></a> `00af5c8c` | `08 a0 00 91` | add x8,x0,#0x28 | `FALL_THROUGH`
<a id="insn-00af5c90"></a> `00af5c90` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00af5c94"></a> `00af5c94` | `1b 08 00 f9` | str x27,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00af5c98"></a> `00af5c98` | `17 20 02 a9` | stp x23,x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00af5c9c"></a> `00af5c9c` | `08 7c 03 a9` | stp x8,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00af5ca0"></a> `00af5ca0` | `40 03 00 f9` | str x0,[x26] | `FALL_THROUGH`
<a id="insn-00af5ca4"></a> `00af5ca4` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00af5ca8"></a> `00af5ca8` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00af5cac"></a> `00af5cac` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00af5cb0"></a> `00af5cb0` | `08 01 00 b4` | cbz x8,0x00af5cd0 | `CONDITIONAL_JUMP`
<a id="insn-00af5cb4"></a> `00af5cb4` | `28 03 00 f9` | str x8,[x25] | `FALL_THROUGH`
<a id="insn-00af5cb8"></a> `00af5cb8` | `41 03 40 f9` | ldr x1,[x26] | `FALL_THROUGH`
<a id="insn-00af5cbc"></a> `00af5cbc` | `06 00 00 14` | b 0x00af5cd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00af5cc0"></a> `00af5cc0` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00af5cc4"></a> `00af5cc4` | `58 03 40 f9` | ldr x24,[x26] | `FALL_THROUGH`
<a id="insn-00af5cc8"></a> `00af5cc8` | `18 01 00 b5` | cbnz x24,0x00af5ce8 | `CONDITIONAL_JUMP`
<a id="insn-00af5ccc"></a> `00af5ccc` | `ee ff ff 17` | b 0x00af5c84 | `UNCONDITIONAL_JUMP`
<a id="insn-00af5cd0"></a> `00af5cd0` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00af5cd4"></a> `00af5cd4` | `20 07 40 f9` | ldr x0,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00af5cd8"></a> `00af5cd8` | `62 a2 03 94` | bl 0x00bde660 | `UNCONDITIONAL_CALL`
<a id="insn-00af5cdc"></a> `00af5cdc` | `28 0b 40 f9` | ldr x8,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00af5ce0"></a> `00af5ce0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00af5ce4"></a> `00af5ce4` | `28 0b 00 f9` | str x8,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00af5ce8"></a> `00af5ce8` | `00 07 80 52` | mov w0,#0x38 | `FALL_THROUGH`
<a id="insn-00af5cec"></a> `00af5cec` | `1a a3 00 91` | add x26,x24,#0x28 | `FALL_THROUGH`
<a id="insn-00af5cf0"></a> `00af5cf0` | `94 94 03 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00af5cf4"></a> `00af5cf4` | `1f fc 02 a9` | stp xzr,xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00af5cf8"></a> `00af5cf8` | `1f 10 00 f9` | str xzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00af5cfc"></a> `00af5cfc` | `1a 04 00 f9` | str x26,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00af5d00"></a> `00af5d00` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00af5d04"></a> `00af5d04` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00af5d08"></a> `00af5d08` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00af5d0c"></a> `00af5d0c` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00af5d10"></a> `00af5d10` | `00 05 00 f9` | str x0,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00af5d14"></a> `00af5d14` | `08 1f 40 f9` | ldr x8,[x24, #0x38] | `FALL_THROUGH`
<a id="insn-00af5d18"></a> `00af5d18` | `00 17 00 f9` | str x0,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00af5d1c"></a> `00af5d1c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00af5d20"></a> `00af5d20` | `08 1f 00 f9` | str x8,[x24, #0x38] | `FALL_THROUGH`
<a id="insn-00af5d24"></a> `00af5d24` | `3f 0f 01 f8` | str xzr,[x25, #0x10]! | `FALL_THROUGH`
<a id="insn-00af5d28"></a> `00af5d28` | `16 80 01 a9` | stp x22,x0,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00af5d2c"></a> `00af5d2c` | `56 2d 00 f0` | adrp x22,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af5d30"></a> `00af5d30` | `d6 22 27 91` | add x22,x22,#0x9c8 | `FALL_THROUGH`
<a id="insn-00af5d34"></a> `00af5d34` | `1a 14 00 f9` | str x26,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00af5d38"></a> `00af5d38` | `1f c0 00 39` | strb wzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00af5d3c"></a> `00af5d3c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00af5d40"></a> `00af5d40` | `7c a2 03 94` | bl 0x00bde730 | `UNCONDITIONAL_CALL`
<a id="insn-00af5d44"></a> `00af5d44` | `48 2d 00 f0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af5d48"></a> `00af5d48` | `49 2d 00 f0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af5d4c"></a> `00af5d4c` | `01 49 41 f9` | ldr x1,[x8, #0x290] | `FALL_THROUGH`
<a id="insn-00af5d50"></a> `00af5d50` | `22 51 41 f9` | ldr x2,[x9, #0x2a0] | `FALL_THROUGH`
<a id="insn-00af5d54"></a> `00af5d54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af5d58"></a> `00af5d58` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00af5d5c"></a> `00af5d5c` | `e4 03 14 aa` | mov x4,x20 | `FALL_THROUGH`
<a id="insn-00af5d60"></a> `00af5d60` | `e5 03 19 aa` | mov x5,x25 | `FALL_THROUGH`
<a id="insn-00af5d64"></a> `00af5d64` | `ae c2 e9 97` | bl 0x0056681c | `UNCONDITIONAL_CALL`
<a id="insn-00af5d68"></a> `00af5d68` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00af5d6c"></a> `00af5d6c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00af5d70"></a> `00af5d70` | `6c a2 03 94` | bl 0x00bde720 | `UNCONDITIONAL_CALL`
<a id="insn-00af5d74"></a> `00af5d74` | `e8 c2 40 39` | ldrb w8,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00af5d78"></a> `00af5d78` | `68 01 00 34` | cbz w8,0x00af5da4 | `CONDITIONAL_JUMP`
<a id="insn-00af5d7c"></a> `00af5d7c` | `e0 22 42 a9` | ldp x0,x8,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00af5d80"></a> `00af5d80` | `09 28 40 a9` | ldp x9,x10,[x0] | `FALL_THROUGH`
<a id="insn-00af5d84"></a> `00af5d84` | `2a 05 00 f9` | str x10,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00af5d88"></a> `00af5d88` | `0a 04 40 f9` | ldr x10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00af5d8c"></a> `00af5d8c` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-00af5d90"></a> `00af5d90` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00af5d94"></a> `00af5d94` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00af5d98"></a> `00af5d98` | `09 09 00 f9` | str x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00af5d9c"></a> `00af5d9c` | `71 94 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00af5da0"></a> `00af5da0` | `07 00 00 14` | b 0x00af5dbc | `UNCONDITIONAL_JUMP`
<a id="insn-00af5da4"></a> `00af5da4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af5da8"></a> `00af5da8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af5dac"></a> `00af5dac` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00af5db0"></a> `00af5db0` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00af5db4"></a> `00af5db4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af5db8"></a> `00af5db8` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00af5dbc"></a> `00af5dbc` | `40 2d 00 f0` | adrp x0,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af5dc0"></a> `00af5dc0` | `00 20 27 91` | add x0,x0,#0x9c8 | `FALL_THROUGH`
<a id="insn-00af5dc4"></a> `00af5dc4` | `5b a2 03 94` | bl 0x00bde730 | `UNCONDITIONAL_CALL`
<a id="insn-00af5dc8"></a> `00af5dc8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af5dcc"></a> `00af5dcc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af5dd0"></a> `00af5dd0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00af5dd4"></a> `00af5dd4` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00af5dd8"></a> `00af5dd8` | `02 5d 40 f9` | ldr x2,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00af5ddc"></a> `00af5ddc` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00af5de0"></a> `00af5de0` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af5de4"></a> `00af5de4` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af5de8"></a> `00af5de8` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af5dec"></a> `00af5dec` | `fb 07 46 f8` | ldr x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00af5df0"></a> `00af5df0` | `40 00 1f d6` | br x2 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00af5bec`](#insn-00af5bec) 範囲 `[['00af5bec', '00af5bf7']]`
  - `FALL_THROUGH` [`00af5bf4`](#insn-00af5bf4) → [`00af5bf8`](#insn-00af5bf8)
- ブロック [`00af5bf8`](#insn-00af5bf8) 範囲 `[['00af5bf8', '00af5c03']]`
  - `FALL_THROUGH` [`00af5c00`](#insn-00af5c00) → [`00af5c04`](#insn-00af5c04)
- ブロック [`00af5c04`](#insn-00af5c04) 範囲 `[['00af5c04', '00af5c0f']]`
  - `FALL_THROUGH` [`00af5c0c`](#insn-00af5c0c) → [`00af5c10`](#insn-00af5c10)
- ブロック [`00af5c10`](#insn-00af5c10) 範囲 `[['00af5c10', '00af5c1b']]`
  - `FALL_THROUGH` [`00af5c18`](#insn-00af5c18) → [`00af5c1c`](#insn-00af5c1c)
- ブロック [`00af5c1c`](#insn-00af5c1c) 範囲 `[['00af5c1c', '00af5c27']]`
  - `FALL_THROUGH` [`00af5c24`](#insn-00af5c24) → [`00af5c28`](#insn-00af5c28)
- ブロック [`00af5c28`](#insn-00af5c28) 範囲 `[['00af5c28', '00af5c33']]`
  - `FALL_THROUGH` [`00af5c30`](#insn-00af5c30) → [`00af5c34`](#insn-00af5c34)
- ブロック [`00af5c34`](#insn-00af5c34) 範囲 `[['00af5c34', '00af5c3b']]`
  - `CONDITIONAL_JUMP` [`00af5c38`](#insn-00af5c38) → [`00af5c78`](#insn-00af5c78)
  - `FALL_THROUGH` [`00af5c38`](#insn-00af5c38) → [`00af5c3c`](#insn-00af5c3c)
- ブロック [`00af5c3c`](#insn-00af5c3c) 範囲 `[['00af5c3c', '00af5c3f']]`
  - `FALL_THROUGH` [`00af5c3c`](#insn-00af5c3c) → [`00af5c40`](#insn-00af5c40)
- ブロック [`00af5c40`](#insn-00af5c40) 範囲 `[['00af5c40', '00af5c4b']]`
  - `CONDITIONAL_JUMP` [`00af5c48`](#insn-00af5c48) → [`00af5c60`](#insn-00af5c60)
  - `FALL_THROUGH` [`00af5c48`](#insn-00af5c48) → [`00af5c4c`](#insn-00af5c4c)
- ブロック [`00af5c4c`](#insn-00af5c4c) 範囲 `[['00af5c4c', '00af5c53']]`
  - `CONDITIONAL_JUMP` [`00af5c50`](#insn-00af5c50) → [`00af5cc0`](#insn-00af5cc0)
  - `FALL_THROUGH` [`00af5c50`](#insn-00af5c50) → [`00af5c54`](#insn-00af5c54)
- ブロック [`00af5c54`](#insn-00af5c54) 範囲 `[['00af5c54', '00af5c5f']]`
  - `UNCONDITIONAL_JUMP` [`00af5c5c`](#insn-00af5c5c) → [`00af5c40`](#insn-00af5c40)
- ブロック [`00af5c60`](#insn-00af5c60) 範囲 `[['00af5c60', '00af5c63']]`
  - `CONDITIONAL_JUMP` [`00af5c60`](#insn-00af5c60) → [`00af5c7c`](#insn-00af5c7c)
  - `FALL_THROUGH` [`00af5c60`](#insn-00af5c60) → [`00af5c64`](#insn-00af5c64)
- ブロック [`00af5c64`](#insn-00af5c64) 範囲 `[['00af5c64', '00af5c6f']]`
  - `CONDITIONAL_JUMP` [`00af5c6c`](#insn-00af5c6c) → [`00af5c7c`](#insn-00af5c7c)
  - `FALL_THROUGH` [`00af5c6c`](#insn-00af5c6c) → [`00af5c70`](#insn-00af5c70)
- ブロック [`00af5c70`](#insn-00af5c70) 範囲 `[['00af5c70', '00af5c77']]`
  - `UNCONDITIONAL_JUMP` [`00af5c74`](#insn-00af5c74) → [`00af5c40`](#insn-00af5c40)
- ブロック [`00af5c78`](#insn-00af5c78) 範囲 `[['00af5c78', '00af5c7b']]`
  - `FALL_THROUGH` [`00af5c78`](#insn-00af5c78) → [`00af5c7c`](#insn-00af5c7c)
- ブロック [`00af5c7c`](#insn-00af5c7c) 範囲 `[['00af5c7c', '00af5c7f']]`
  - `FALL_THROUGH` [`00af5c7c`](#insn-00af5c7c) → [`00af5c80`](#insn-00af5c80)
- ブロック [`00af5c80`](#insn-00af5c80) 範囲 `[['00af5c80', '00af5c83']]`
  - `CONDITIONAL_JUMP` [`00af5c80`](#insn-00af5c80) → [`00af5ce8`](#insn-00af5ce8)
  - `FALL_THROUGH` [`00af5c80`](#insn-00af5c80) → [`00af5c84`](#insn-00af5c84)
- ブロック [`00af5c84`](#insn-00af5c84) 範囲 `[['00af5c84', '00af5c8b']]`
  - `FALL_THROUGH` [`00af5c88`](#insn-00af5c88) → [`00af5c8c`](#insn-00af5c8c)
- ブロック [`00af5c8c`](#insn-00af5c8c) 範囲 `[['00af5c8c', '00af5c97']]`
  - `FALL_THROUGH` [`00af5c94`](#insn-00af5c94) → [`00af5c98`](#insn-00af5c98)
- ブロック [`00af5c98`](#insn-00af5c98) 範囲 `[['00af5c98', '00af5ca3']]`
  - `FALL_THROUGH` [`00af5ca0`](#insn-00af5ca0) → [`00af5ca4`](#insn-00af5ca4)
- ブロック [`00af5ca4`](#insn-00af5ca4) 範囲 `[['00af5ca4', '00af5caf']]`
  - `FALL_THROUGH` [`00af5cac`](#insn-00af5cac) → [`00af5cb0`](#insn-00af5cb0)
- ブロック [`00af5cb0`](#insn-00af5cb0) 範囲 `[['00af5cb0', '00af5cb3']]`
  - `CONDITIONAL_JUMP` [`00af5cb0`](#insn-00af5cb0) → [`00af5cd0`](#insn-00af5cd0)
  - `FALL_THROUGH` [`00af5cb0`](#insn-00af5cb0) → [`00af5cb4`](#insn-00af5cb4)
- ブロック [`00af5cb4`](#insn-00af5cb4) 範囲 `[['00af5cb4', '00af5cbb']]`
  - `FALL_THROUGH` [`00af5cb8`](#insn-00af5cb8) → [`00af5cbc`](#insn-00af5cbc)
- ブロック [`00af5cbc`](#insn-00af5cbc) 範囲 `[['00af5cbc', '00af5cbf']]`
  - `UNCONDITIONAL_JUMP` [`00af5cbc`](#insn-00af5cbc) → [`00af5cd4`](#insn-00af5cd4)
- ブロック [`00af5cc0`](#insn-00af5cc0) 範囲 `[['00af5cc0', '00af5cc7']]`
  - `FALL_THROUGH` [`00af5cc4`](#insn-00af5cc4) → [`00af5cc8`](#insn-00af5cc8)
- ブロック [`00af5cc8`](#insn-00af5cc8) 範囲 `[['00af5cc8', '00af5ccb']]`
  - `CONDITIONAL_JUMP` [`00af5cc8`](#insn-00af5cc8) → [`00af5ce8`](#insn-00af5ce8)
  - `FALL_THROUGH` [`00af5cc8`](#insn-00af5cc8) → [`00af5ccc`](#insn-00af5ccc)
- ブロック [`00af5ccc`](#insn-00af5ccc) 範囲 `[['00af5ccc', '00af5ccf']]`
  - `UNCONDITIONAL_JUMP` [`00af5ccc`](#insn-00af5ccc) → [`00af5c84`](#insn-00af5c84)
- ブロック [`00af5cd0`](#insn-00af5cd0) 範囲 `[['00af5cd0', '00af5cd3']]`
  - `FALL_THROUGH` [`00af5cd0`](#insn-00af5cd0) → [`00af5cd4`](#insn-00af5cd4)
- ブロック [`00af5cd4`](#insn-00af5cd4) 範囲 `[['00af5cd4', '00af5cdf']]`
  - `FALL_THROUGH` [`00af5cdc`](#insn-00af5cdc) → [`00af5ce0`](#insn-00af5ce0)
- ブロック [`00af5ce0`](#insn-00af5ce0) 範囲 `[['00af5ce0', '00af5ce7']]`
  - `FALL_THROUGH` [`00af5ce4`](#insn-00af5ce4) → [`00af5ce8`](#insn-00af5ce8)
- ブロック [`00af5ce8`](#insn-00af5ce8) 範囲 `[['00af5ce8', '00af5ceb']]`
  - `FALL_THROUGH` [`00af5ce8`](#insn-00af5ce8) → [`00af5cec`](#insn-00af5cec)
- ブロック [`00af5cec`](#insn-00af5cec) 範囲 `[['00af5cec', '00af5cf7']]`
  - `FALL_THROUGH` [`00af5cf4`](#insn-00af5cf4) → [`00af5cf8`](#insn-00af5cf8)
- ブロック [`00af5cf8`](#insn-00af5cf8) 範囲 `[['00af5cf8', '00af5d03']]`
  - `FALL_THROUGH` [`00af5d00`](#insn-00af5d00) → [`00af5d04`](#insn-00af5d04)
- ブロック [`00af5d04`](#insn-00af5d04) 範囲 `[['00af5d04', '00af5d1f']]`
  - `FALL_THROUGH` [`00af5d1c`](#insn-00af5d1c) → [`00af5d20`](#insn-00af5d20)
- ブロック [`00af5d20`](#insn-00af5d20) 範囲 `[['00af5d20', '00af5d2b']]`
  - `FALL_THROUGH` [`00af5d28`](#insn-00af5d28) → [`00af5d2c`](#insn-00af5d2c)
- ブロック [`00af5d2c`](#insn-00af5d2c) 範囲 `[['00af5d2c', '00af5d3f']]`
  - `FALL_THROUGH` [`00af5d3c`](#insn-00af5d3c) → [`00af5d40`](#insn-00af5d40)
- ブロック [`00af5d40`](#insn-00af5d40) 範囲 `[['00af5d40', '00af5d5b']]`
  - `FALL_THROUGH` [`00af5d58`](#insn-00af5d58) → [`00af5d5c`](#insn-00af5d5c)
- ブロック [`00af5d5c`](#insn-00af5d5c) 範囲 `[['00af5d5c', '00af5d63']]`
  - `FALL_THROUGH` [`00af5d60`](#insn-00af5d60) → [`00af5d64`](#insn-00af5d64)
- ブロック [`00af5d64`](#insn-00af5d64) 範囲 `[['00af5d64', '00af5d7b']]`
  - `CONDITIONAL_JUMP` [`00af5d78`](#insn-00af5d78) → [`00af5da4`](#insn-00af5da4)
  - `FALL_THROUGH` [`00af5d78`](#insn-00af5d78) → [`00af5d7c`](#insn-00af5d7c)
- ブロック [`00af5d7c`](#insn-00af5d7c) 範囲 `[['00af5d7c', '00af5da3']]`
  - `UNCONDITIONAL_JUMP` [`00af5da0`](#insn-00af5da0) → [`00af5dbc`](#insn-00af5dbc)
- ブロック [`00af5da4`](#insn-00af5da4) 範囲 `[['00af5da4', '00af5dbb']]`
  - `FALL_THROUGH` [`00af5db8`](#insn-00af5db8) → [`00af5dbc`](#insn-00af5dbc)
- ブロック [`00af5dbc`](#insn-00af5dbc) 範囲 `[['00af5dbc', '00af5df3']]`

## 命令位置別の参照

- [`00af5bec`](#insn-00af5bec) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5bf0`](#insn-00af5bf0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5bf4`](#insn-00af5bf4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5bf8`](#insn-00af5bf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5bfc`](#insn-00af5bfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c00`](#insn-00af5c00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c10`](#insn-00af5c10) → `010a09c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c24`](#insn-00af5c24) → [`00bde720`](../00bde/00bde720.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde720` · 推定シンボル `None` · 推定型 `None`
- [`00af5c2c`](#insn-00af5c2c) → `010a09c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af5c38`](#insn-00af5c38) → [`00af5c78`](#insn-00af5c78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c48`](#insn-00af5c48) → [`00af5c60`](#insn-00af5c60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c50`](#insn-00af5c50) → [`00af5cc0`](#insn-00af5cc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c5c`](#insn-00af5c5c) → [`00af5c40`](#insn-00af5c40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c60`](#insn-00af5c60) → [`00af5c7c`](#insn-00af5c7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c6c`](#insn-00af5c6c) → [`00af5c7c`](#insn-00af5c7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c74`](#insn-00af5c74) → [`00af5c40`](#insn-00af5c40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c80`](#insn-00af5c80) → [`00af5ce8`](#insn-00af5ce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c88`](#insn-00af5c88) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00af5cb0`](#insn-00af5cb0) → [`00af5cd0`](#insn-00af5cd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5cbc`](#insn-00af5cbc) → [`00af5cd4`](#insn-00af5cd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5cc8`](#insn-00af5cc8) → [`00af5ce8`](#insn-00af5ce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5ccc`](#insn-00af5ccc) → [`00af5c84`](#insn-00af5c84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5cd8`](#insn-00af5cd8) → [`00bde660`](../00bde/00bde660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde660` · 推定シンボル `None` · 推定型 `None`
- [`00af5cf0`](#insn-00af5cf0) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00af5d3c`](#insn-00af5d3c) → `010a09c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5d40`](#insn-00af5d40) → [`00bde730`](../00bde/00bde730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde730` · 推定シンボル `None` · 推定型 `None`
- [`00af5d4c`](#insn-00af5d4c) → `010a0290`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af5d50`](#insn-00af5d50) → `010a02a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af5d64`](#insn-00af5d64) → [`0056681c`](../00566/0056681c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0056681c` · 推定シンボル `None` · 推定型 `None`
- [`00af5d6c`](#insn-00af5d6c) → `010a09c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5d70`](#insn-00af5d70) → [`00bde720`](../00bde/00bde720.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde720` · 推定シンボル `None` · 推定型 `None`
- [`00af5d78`](#insn-00af5d78) → [`00af5da4`](#insn-00af5da4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5d9c`](#insn-00af5d9c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00af5da0`](#insn-00af5da0) → [`00af5dbc`](#insn-00af5dbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5dc0`](#insn-00af5dc0) → `010a09c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5dc4`](#insn-00af5dc4) → [`00bde730`](../00bde/00bde730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde730` · 推定シンボル `None` · 推定型 `None`
- [`00af5dd4`](#insn-00af5dd4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5ddc`](#insn-00af5ddc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5de0`](#insn-00af5de0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5de4`](#insn-00af5de4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5de8`](#insn-00af5de8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af5bec`](#insn-00af5bec)

~~~json
{
  "source": "00af5bec",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5bf0`](#insn-00af5bf0)

~~~json
{
  "source": "00af5bf0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5bf4`](#insn-00af5bf4)

~~~json
{
  "source": "00af5bf4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5bf8`](#insn-00af5bf8)

~~~json
{
  "source": "00af5bf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5bfc`](#insn-00af5bfc)

~~~json
{
  "source": "00af5bfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c00`](#insn-00af5c00)

~~~json
{
  "source": "00af5c00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c10`](#insn-00af5c10)

~~~json
{
  "source": "00af5c10",
  "target": "010a09c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c24`](#insn-00af5c24)

~~~json
{
  "source": "00af5c24",
  "target": "00bde720",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5c2c`](#insn-00af5c2c)

~~~json
{
  "source": "00af5c2c",
  "target": "010a09c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af5c38`](#insn-00af5c38)

~~~json
{
  "source": "00af5c38",
  "target": "00af5c78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c48`](#insn-00af5c48)

~~~json
{
  "source": "00af5c48",
  "target": "00af5c60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c50`](#insn-00af5c50)

~~~json
{
  "source": "00af5c50",
  "target": "00af5cc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c5c`](#insn-00af5c5c)

~~~json
{
  "source": "00af5c5c",
  "target": "00af5c40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c60`](#insn-00af5c60)

~~~json
{
  "source": "00af5c60",
  "target": "00af5c7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c6c`](#insn-00af5c6c)

~~~json
{
  "source": "00af5c6c",
  "target": "00af5c7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c74`](#insn-00af5c74)

~~~json
{
  "source": "00af5c74",
  "target": "00af5c40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c80`](#insn-00af5c80)

~~~json
{
  "source": "00af5c80",
  "target": "00af5ce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c88`](#insn-00af5c88)

~~~json
{
  "source": "00af5c88",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5cb0`](#insn-00af5cb0)

~~~json
{
  "source": "00af5cb0",
  "target": "00af5cd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5cbc`](#insn-00af5cbc)

~~~json
{
  "source": "00af5cbc",
  "target": "00af5cd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5cc8`](#insn-00af5cc8)

~~~json
{
  "source": "00af5cc8",
  "target": "00af5ce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5ccc`](#insn-00af5ccc)

~~~json
{
  "source": "00af5ccc",
  "target": "00af5c84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5cd8`](#insn-00af5cd8)

~~~json
{
  "source": "00af5cd8",
  "target": "00bde660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5cf0`](#insn-00af5cf0)

~~~json
{
  "source": "00af5cf0",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5d3c`](#insn-00af5d3c)

~~~json
{
  "source": "00af5d3c",
  "target": "010a09c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5d40`](#insn-00af5d40)

~~~json
{
  "source": "00af5d40",
  "target": "00bde730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5d4c`](#insn-00af5d4c)

~~~json
{
  "source": "00af5d4c",
  "target": "010a0290",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0290",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af5d50`](#insn-00af5d50)

~~~json
{
  "source": "00af5d50",
  "target": "010a02a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a02a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af5d64`](#insn-00af5d64)

~~~json
{
  "source": "00af5d64",
  "target": "0056681c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5d6c`](#insn-00af5d6c)

~~~json
{
  "source": "00af5d6c",
  "target": "010a09c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5d70`](#insn-00af5d70)

~~~json
{
  "source": "00af5d70",
  "target": "00bde720",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5d78`](#insn-00af5d78)

~~~json
{
  "source": "00af5d78",
  "target": "00af5da4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5d9c`](#insn-00af5d9c)

~~~json
{
  "source": "00af5d9c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5da0`](#insn-00af5da0)

~~~json
{
  "source": "00af5da0",
  "target": "00af5dbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5dc0`](#insn-00af5dc0)

~~~json
{
  "source": "00af5dc0",
  "target": "010a09c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5dc4`](#insn-00af5dc4)

~~~json
{
  "source": "00af5dc4",
  "target": "00bde730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5dd4`](#insn-00af5dd4)

~~~json
{
  "source": "00af5dd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5ddc`](#insn-00af5ddc)

~~~json
{
  "source": "00af5ddc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5de0`](#insn-00af5de0)

~~~json
{
  "source": "00af5de0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5de4`](#insn-00af5de4)

~~~json
{
  "source": "00af5de4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5de8`](#insn-00af5de8)

~~~json
{
  "source": "00af5de8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
