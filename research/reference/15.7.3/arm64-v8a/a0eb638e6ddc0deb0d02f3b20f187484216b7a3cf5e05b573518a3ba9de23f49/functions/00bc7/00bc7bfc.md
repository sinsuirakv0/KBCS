# 00bc7bfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bc7b34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7b34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-c8bb54e1398f7fb5da5cdb987bb33662)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bc7c40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7c40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-dabe1c3be6b7c86a462eebe5d5bcf550)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc7bfc",
  "name": "FUN_00bc7bfc",
  "size": 812,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "931fb9854a63b451a7f5235ada1e0547e7db53d93126d53544f0d57a019334a2",
  "source_text_sha256": "931fb9854a63b451a7f5235ada1e0547e7db53d93126d53544f0d57a019334a2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc7bfc",
        "00bc7f27"
      ]
    ],
    "bytes_sha256": "b3cd4cb5a55f06486b807bc0856de82920692d867d3adaacb287b5001eb834aa",
    "instruction_count": 203,
    "instruction_bytes": 812,
    "body_bytes": 812,
    "indirect": 8,
    "unresolved": 8
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb160](../00bdb/00bdb160.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6994 bytes

~~~c

void FUN_00bc7bfc(long param_1,undefined8 *param_2)

{
  void *pvVar1;
  size_t __size;
  long lVar2;
  long lVar3;
  ulong uVar4;
  long *plVar5;
  size_t sVar6;
  void *__src;
  
  plVar5 = *(long **)(param_1 + 0x10);
  if ((uint)((int)((uint)*(ushort *)((long)plVar5 + 9) << 0x1a) >> 0x1a) <
      ((int)((uint)*(ushort *)(param_1 + 9) << 0x1a) >> 0x1a) + 1U) {
    (**(code **)(*plVar5 + 0x20))(plVar5,param_2);
    if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
      (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
    }
    sVar6 = *(size_t *)(param_1 + 0x20);
  }
  else {
    lVar2 = param_2[1];
    pvVar1 = (void *)*param_2;
    uVar4 = lVar2 + 1;
    *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + 1;
    if ((ulong)param_2[2] < uVar4) {
      sVar6 = param_2[2] * 2;
      uVar4 = lVar2 + 0x3e1;
      if (sVar6 < uVar4 || sVar6 - uVar4 == 0) {
        sVar6 = uVar4;
      }
      param_2[2] = sVar6;
      pvVar1 = realloc(pvVar1,sVar6);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
    lVar3 = *plVar5;
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x28;
                    /* try { // try from 00bc7cdc to 00cc7ce3 has its CatchHandler @ 00bc8d4c */
    (**(code **)(lVar3 + 0x20))(plVar5,param_2);
    if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
                    /* try { // try from 00bc7cf8 to 00cc7cff has its CatchHandler @ 00bc8d44 */
      (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
    }
    lVar2 = param_2[1];
    pvVar1 = (void *)*param_2;
                    /* try { // try from 00bc7d14 to 00cc7d1b has its CatchHandler @ 00bc8d48 */
    uVar4 = lVar2 + 1;
    *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + -1;
    if ((ulong)param_2[2] < uVar4) {
      sVar6 = param_2[2] * 2;
      uVar4 = lVar2 + 0x3e1;
                    /* try { // try from 00bc7d30 to 00cc7d37 has its CatchHandler @ 00bc8d40 */
      if (sVar6 < uVar4 || sVar6 - uVar4 == 0) {
        sVar6 = uVar4;
      }
      param_2[2] = sVar6;
      pvVar1 = realloc(pvVar1,sVar6);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
                    /* try { // try from 00bc7d4c to 00cc7d53 has its CatchHandler @ 00bc8d3c */
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x29;
    sVar6 = *(size_t *)(param_1 + 0x20);
  }
  if (sVar6 != 0) {
    lVar2 = param_2[1];
                    /* try { // try from 00bc7d68 to 00cc7d6f has its CatchHandler @ 00bc8d38 */
    pvVar1 = (void *)*param_2;
    __src = *(void **)(param_1 + 0x18);
    if ((ulong)param_2[2] < lVar2 + sVar6) {
      __size = param_2[2] * 2;
      uVar4 = lVar2 + sVar6 + 0x3e0;
                    /* try { // try from 00bc7d84 to 00cc7d87 has its CatchHandler @ 00bc8d48 */
      if (__size < uVar4 || __size - uVar4 == 0) {
        __size = uVar4;
      }
      param_2[2] = __size;
      pvVar1 = realloc(pvVar1,__size);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bc7f14 to 00cc7f1b has its CatchHandler @ 00bc8c28 */
        abort();
      }
                    /* try { // try from 00bc7d9c to 00cc7d9f has its CatchHandler @ 00bc8d4c */
      lVar2 = param_2[1];
    }
    memcpy((void *)((long)pvVar1 + lVar2),__src,sVar6);
                    /* try { // try from 00bc7db4 to 00cc7db7 has its CatchHandler @ 00bc8d44 */
    param_2[1] = param_2[1] + sVar6;
  }
  plVar5 = *(long **)(param_1 + 0x28);
                    /* try { // try from 00bc7dcc to 00cc7dcf has its CatchHandler @ 00bc8d40 */
  if ((*(ushort *)((long)plVar5 + 9) & 0x3f) < (*(ushort *)(param_1 + 9) & 0x3f)) {
                    /* try { // try from 00bc7de4 to 00cc7de7 has its CatchHandler @ 00bc8d38 */
    (**(code **)(*plVar5 + 0x20))(plVar5,param_2);
    if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
                    /* try { // try from 00bc7dfc to 00cc7dff has its CatchHandler @ 00bc8d3c */
                    /* try { // try from 00bc7e14 to 00cc7e17 has its CatchHandler @ 00bc8c94 */
                    /* WARNING: Could not recover jumptable at 0x00bc7e1c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
      return;
    }
  }
  else {
    lVar2 = param_2[1];
    pvVar1 = (void *)*param_2;
                    /* try { // try from 00bc7e2c to 00cc7e33 has its CatchHandler @ 00bc8c7c */
    uVar4 = lVar2 + 1;
    *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + 1;
    if ((ulong)param_2[2] < uVar4) {
      sVar6 = param_2[2] * 2;
      uVar4 = lVar2 + 0x3e1;
                    /* try { // try from 00bc7e48 to 00cc7e4f has its CatchHandler @ 00bc8c78 */
      if (sVar6 < uVar4 || sVar6 - uVar4 == 0) {
        sVar6 = uVar4;
      }
      param_2[2] = sVar6;
      pvVar1 = realloc(pvVar1,sVar6);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
                    /* try { // try from 00bc7e64 to 00cc7e6b has its CatchHandler @ 00bc8c74 */
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
    lVar3 = *plVar5;
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x28;
                    /* try { // try from 00bc7e80 to 00cc7e87 has its CatchHandler @ 00bc8c70 */
    (**(code **)(lVar3 + 0x20))(plVar5,param_2);
    if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
                    /* try { // try from 00bc7e9c to 00cc7e9f has its CatchHandler @ 00bc8c94 */
      (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
    }
    lVar2 = param_2[1];
                    /* try { // try from 00bc7eb4 to 00cc7eb7 has its CatchHandler @ 00bc8c7c */
    pvVar1 = (void *)*param_2;
    uVar4 = lVar2 + 1;
    *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + -1;
    if ((ulong)param_2[2] < uVar4) {
                    /* try { // try from 00bc7ecc to 00cc7ecf has its CatchHandler @ 00bc8c78 */
      sVar6 = param_2[2] * 2;
      uVar4 = lVar2 + 0x3e1;
      if (sVar6 < uVar4 || sVar6 - uVar4 == 0) {
        sVar6 = uVar4;
      }
      param_2[2] = sVar6;
      pvVar1 = realloc(pvVar1,sVar6);
                    /* try { // try from 00bc7ee4 to 00cc7ee7 has its CatchHandler @ 00bc8c74 */
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
                    /* try { // try from 00bc7efc to 00cc7eff has its CatchHandler @ 00bc8c70 */
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x29;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc7bfc"></a> `00bc7bfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bc7c00"></a> `00bc7c00` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bc7c04"></a> `00bc7c04` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc7c08"></a> `00bc7c08` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7c0c"></a> `00bc7c0c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bc7c10"></a> `00bc7c10` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bc7c14"></a> `00bc7c14` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bc7c18"></a> `00bc7c18` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bc7c1c"></a> `00bc7c1c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bc7c20"></a> `00bc7c20` | `a9 92 40 78` | ldurh w9,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bc7c24"></a> `00bc7c24` | `08 15 00 13` | sbfx w8,w8,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bc7c28"></a> `00bc7c28` | `29 15 06 53` | lsl w9,w9,#0x1a | `FALL_THROUGH`
<a id="insn-00bc7c2c"></a> `00bc7c2c` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7c30"></a> `00bc7c30` | `1f 69 89 6b` | cmp w8,w9, ASR #0x1a | `FALL_THROUGH`
<a id="insn-00bc7c34"></a> `00bc7c34` | `49 02 00 54` | b.ls 0x00bc7c7c | `CONDITIONAL_JUMP`
<a id="insn-00bc7c38"></a> `00bc7c38` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc7c3c"></a> `00bc7c3c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7c40"></a> `00bc7c40` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc7c44"></a> `00bc7c44` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7c48"></a> `00bc7c48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc7c4c"></a> `00bc7c4c` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bc7c50"></a> `00bc7c50` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bc7c54"></a> `00bc7c54` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bc7c58"></a> `00bc7c58` | `c0 00 00 54` | b.eq 0x00bc7c70 | `CONDITIONAL_JUMP`
<a id="insn-00bc7c5c"></a> `00bc7c5c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc7c60"></a> `00bc7c60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7c64"></a> `00bc7c64` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc7c68"></a> `00bc7c68` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bc7c6c"></a> `00bc7c6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc7c70"></a> `00bc7c70` | `95 12 40 f9` | ldr x21,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7c74"></a> `00bc7c74` | `95 07 00 b5` | cbnz x21,0x00bc7d64 | `CONDITIONAL_JUMP`
<a id="insn-00bc7c78"></a> `00bc7c78` | `51 00 00 14` | b 0x00bc7dbc | `UNCONDITIONAL_JUMP`
<a id="insn-00bc7c7c"></a> `00bc7c7c` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7c80"></a> `00bc7c80` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7c84"></a> `00bc7c84` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bc7c88"></a> `00bc7c88` | `6b 05 00 11` | add w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7c8c"></a> `00bc7c8c` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7c90"></a> `00bc7c90` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7c94"></a> `00bc7c94` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bc7c98"></a> `00bc7c98` | `69 01 00 54` | b.ls 0x00bc7cc4 | `CONDITIONAL_JUMP`
<a id="insn-00bc7c9c"></a> `00bc7c9c` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7ca0"></a> `00bc7ca0` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bc7ca4"></a> `00bc7ca4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc7ca8"></a> `00bc7ca8` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bc7cac"></a> `00bc7cac` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bc7cb0"></a> `00bc7cb0` | `54 55 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7cb4"></a> `00bc7cb4` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bc7cb8"></a> `00bc7cb8` | `00 13 00 b4` | cbz x0,0x00bc7f18 | `CONDITIONAL_JUMP`
<a id="insn-00bc7cbc"></a> `00bc7cbc` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7cc0"></a> `00bc7cc0` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7cc4"></a> `00bc7cc4` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7cc8"></a> `00bc7cc8` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00bc7ccc"></a> `00bc7ccc` | `0a 05 80 52` | mov w10,#0x28 | `FALL_THROUGH`
<a id="insn-00bc7cd0"></a> `00bc7cd0` | `0a 68 28 38` | strb w10,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bc7cd4"></a> `00bc7cd4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7cd8"></a> `00bc7cd8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc7cdc"></a> `00bc7cdc` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7ce0"></a> `00bc7ce0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc7ce4"></a> `00bc7ce4` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bc7ce8"></a> `00bc7ce8` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bc7cec"></a> `00bc7cec` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bc7cf0"></a> `00bc7cf0` | `c0 00 00 54` | b.eq 0x00bc7d08 | `CONDITIONAL_JUMP`
<a id="insn-00bc7cf4"></a> `00bc7cf4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc7cf8"></a> `00bc7cf8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7cfc"></a> `00bc7cfc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc7d00"></a> `00bc7d00` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bc7d04"></a> `00bc7d04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc7d08"></a> `00bc7d08` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7d0c"></a> `00bc7d0c` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7d10"></a> `00bc7d10` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bc7d14"></a> `00bc7d14` | `6b 05 00 51` | sub w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7d18"></a> `00bc7d18` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7d1c"></a> `00bc7d1c` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7d20"></a> `00bc7d20` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bc7d24"></a> `00bc7d24` | `69 01 00 54` | b.ls 0x00bc7d50 | `CONDITIONAL_JUMP`
<a id="insn-00bc7d28"></a> `00bc7d28` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7d2c"></a> `00bc7d2c` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bc7d30"></a> `00bc7d30` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc7d34"></a> `00bc7d34` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bc7d38"></a> `00bc7d38` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bc7d3c"></a> `00bc7d3c` | `31 55 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7d40"></a> `00bc7d40` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bc7d44"></a> `00bc7d44` | `c0 0e 00 b4` | cbz x0,0x00bc7f1c | `CONDITIONAL_JUMP`
<a id="insn-00bc7d48"></a> `00bc7d48` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7d4c"></a> `00bc7d4c` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7d50"></a> `00bc7d50` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7d54"></a> `00bc7d54` | `29 05 80 52` | mov w9,#0x29 | `FALL_THROUGH`
<a id="insn-00bc7d58"></a> `00bc7d58` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bc7d5c"></a> `00bc7d5c` | `95 12 40 f9` | ldr x21,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7d60"></a> `00bc7d60` | `f5 02 00 b4` | cbz x21,0x00bc7dbc | `CONDITIONAL_JUMP`
<a id="insn-00bc7d64"></a> `00bc7d64` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7d68"></a> `00bc7d68` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bc7d6c"></a> `00bc7d6c` | `96 0e 40 f9` | ldr x22,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bc7d70"></a> `00bc7d70` | `0a 01 15 8b` | add x10,x8,x21 | `FALL_THROUGH`
<a id="insn-00bc7d74"></a> `00bc7d74` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bc7d78"></a> `00bc7d78` | `49 01 00 54` | b.ls 0x00bc7da0 | `CONDITIONAL_JUMP`
<a id="insn-00bc7d7c"></a> `00bc7d7c` | `28 f9 7f d3` | lsl x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7d80"></a> `00bc7d80` | `49 81 0f 91` | add x9,x10,#0x3e0 | `FALL_THROUGH`
<a id="insn-00bc7d84"></a> `00bc7d84` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bc7d88"></a> `00bc7d88` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00bc7d8c"></a> `00bc7d8c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bc7d90"></a> `00bc7d90` | `1c 55 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7d94"></a> `00bc7d94` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bc7d98"></a> `00bc7d98` | `e0 0b 00 b4` | cbz x0,0x00bc7f14 | `CONDITIONAL_JUMP`
<a id="insn-00bc7d9c"></a> `00bc7d9c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7da0"></a> `00bc7da0` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00bc7da4"></a> `00bc7da4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bc7da8"></a> `00bc7da8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bc7dac"></a> `00bc7dac` | `ed 4c 00 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7db0"></a> `00bc7db0` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7db4"></a> `00bc7db4` | `08 01 15 8b` | add x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00bc7db8"></a> `00bc7db8` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7dbc"></a> `00bc7dbc` | `95 16 40 f9` | ldr x21,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bc7dc0"></a> `00bc7dc0` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bc7dc4"></a> `00bc7dc4` | `a9 92 40 78` | ldurh w9,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bc7dc8"></a> `00bc7dc8` | `08 15 16 53` | ubfiz w8,w8,#0xa,#0x6 | `FALL_THROUGH`
<a id="insn-00bc7dcc"></a> `00bc7dcc` | `29 15 16 53` | ubfiz w9,w9,#0xa,#0x6 | `FALL_THROUGH`
<a id="insn-00bc7dd0"></a> `00bc7dd0` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bc7dd4"></a> `00bc7dd4` | `69 02 00 54` | b.ls 0x00bc7e20 | `CONDITIONAL_JUMP`
<a id="insn-00bc7dd8"></a> `00bc7dd8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc7ddc"></a> `00bc7ddc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7de0"></a> `00bc7de0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc7de4"></a> `00bc7de4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7de8"></a> `00bc7de8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc7dec"></a> `00bc7dec` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bc7df0"></a> `00bc7df0` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bc7df4"></a> `00bc7df4` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bc7df8"></a> `00bc7df8` | `40 08 00 54` | b.eq 0x00bc7f00 | `CONDITIONAL_JUMP`
<a id="insn-00bc7dfc"></a> `00bc7dfc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc7e00"></a> `00bc7e00` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7e04"></a> `00bc7e04` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bc7e08"></a> `00bc7e08` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc7e0c"></a> `00bc7e0c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7e10"></a> `00bc7e10` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc7e14"></a> `00bc7e14` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bc7e18"></a> `00bc7e18` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bc7e1c"></a> `00bc7e1c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bc7e20"></a> `00bc7e20` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7e24"></a> `00bc7e24` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7e28"></a> `00bc7e28` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bc7e2c"></a> `00bc7e2c` | `6b 05 00 11` | add w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7e30"></a> `00bc7e30` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7e34"></a> `00bc7e34` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7e38"></a> `00bc7e38` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bc7e3c"></a> `00bc7e3c` | `69 01 00 54` | b.ls 0x00bc7e68 | `CONDITIONAL_JUMP`
<a id="insn-00bc7e40"></a> `00bc7e40` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7e44"></a> `00bc7e44` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bc7e48"></a> `00bc7e48` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc7e4c"></a> `00bc7e4c` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bc7e50"></a> `00bc7e50` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bc7e54"></a> `00bc7e54` | `eb 54 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7e58"></a> `00bc7e58` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bc7e5c"></a> `00bc7e5c` | `20 06 00 b4` | cbz x0,0x00bc7f20 | `CONDITIONAL_JUMP`
<a id="insn-00bc7e60"></a> `00bc7e60` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7e64"></a> `00bc7e64` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7e68"></a> `00bc7e68` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7e6c"></a> `00bc7e6c` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00bc7e70"></a> `00bc7e70` | `0a 05 80 52` | mov w10,#0x28 | `FALL_THROUGH`
<a id="insn-00bc7e74"></a> `00bc7e74` | `0a 68 28 38` | strb w10,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bc7e78"></a> `00bc7e78` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7e7c"></a> `00bc7e7c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc7e80"></a> `00bc7e80` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7e84"></a> `00bc7e84` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc7e88"></a> `00bc7e88` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bc7e8c"></a> `00bc7e8c` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bc7e90"></a> `00bc7e90` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bc7e94"></a> `00bc7e94` | `c0 00 00 54` | b.eq 0x00bc7eac | `CONDITIONAL_JUMP`
<a id="insn-00bc7e98"></a> `00bc7e98` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc7e9c"></a> `00bc7e9c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7ea0"></a> `00bc7ea0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc7ea4"></a> `00bc7ea4` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bc7ea8"></a> `00bc7ea8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc7eac"></a> `00bc7eac` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7eb0"></a> `00bc7eb0` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7eb4"></a> `00bc7eb4` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bc7eb8"></a> `00bc7eb8` | `6b 05 00 51` | sub w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7ebc"></a> `00bc7ebc` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7ec0"></a> `00bc7ec0` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7ec4"></a> `00bc7ec4` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bc7ec8"></a> `00bc7ec8` | `69 01 00 54` | b.ls 0x00bc7ef4 | `CONDITIONAL_JUMP`
<a id="insn-00bc7ecc"></a> `00bc7ecc` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7ed0"></a> `00bc7ed0` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bc7ed4"></a> `00bc7ed4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc7ed8"></a> `00bc7ed8` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bc7edc"></a> `00bc7edc` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bc7ee0"></a> `00bc7ee0` | `c8 54 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7ee4"></a> `00bc7ee4` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bc7ee8"></a> `00bc7ee8` | `e0 01 00 b4` | cbz x0,0x00bc7f24 | `CONDITIONAL_JUMP`
<a id="insn-00bc7eec"></a> `00bc7eec` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7ef0"></a> `00bc7ef0` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7ef4"></a> `00bc7ef4` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7ef8"></a> `00bc7ef8` | `29 05 80 52` | mov w9,#0x29 | `FALL_THROUGH`
<a id="insn-00bc7efc"></a> `00bc7efc` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bc7f00"></a> `00bc7f00` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc7f04"></a> `00bc7f04` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc7f08"></a> `00bc7f08` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bc7f0c"></a> `00bc7f0c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bc7f10"></a> `00bc7f10` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc7f14"></a> `00bc7f14` | `d7 58 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bc7f18"></a> `00bc7f18` | `d6 58 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bc7f1c"></a> `00bc7f1c` | `d5 58 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bc7f20"></a> `00bc7f20` | `d4 58 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bc7f24"></a> `00bc7f24` | `d3 58 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc7bfc`](#insn-00bc7bfc) 範囲 `[['00bc7bfc', '00bc7c37']]`
  - `CONDITIONAL_JUMP` [`00bc7c34`](#insn-00bc7c34) → [`00bc7c7c`](#insn-00bc7c7c)
  - `FALL_THROUGH` [`00bc7c34`](#insn-00bc7c34) → [`00bc7c38`](#insn-00bc7c38)
- ブロック [`00bc7c38`](#insn-00bc7c38) 範囲 `[['00bc7c38', '00bc7c5b']]`
  - `CONDITIONAL_JUMP` [`00bc7c58`](#insn-00bc7c58) → [`00bc7c70`](#insn-00bc7c70)
  - `FALL_THROUGH` [`00bc7c58`](#insn-00bc7c58) → [`00bc7c5c`](#insn-00bc7c5c)
- ブロック [`00bc7c5c`](#insn-00bc7c5c) 範囲 `[['00bc7c5c', '00bc7c6f']]`
  - `FALL_THROUGH` [`00bc7c6c`](#insn-00bc7c6c) → [`00bc7c70`](#insn-00bc7c70)
- ブロック [`00bc7c70`](#insn-00bc7c70) 範囲 `[['00bc7c70', '00bc7c77']]`
  - `CONDITIONAL_JUMP` [`00bc7c74`](#insn-00bc7c74) → [`00bc7d64`](#insn-00bc7d64)
  - `FALL_THROUGH` [`00bc7c74`](#insn-00bc7c74) → [`00bc7c78`](#insn-00bc7c78)
- ブロック [`00bc7c78`](#insn-00bc7c78) 範囲 `[['00bc7c78', '00bc7c7b']]`
  - `UNCONDITIONAL_JUMP` [`00bc7c78`](#insn-00bc7c78) → [`00bc7dbc`](#insn-00bc7dbc)
- ブロック [`00bc7c7c`](#insn-00bc7c7c) 範囲 `[['00bc7c7c', '00bc7c9b']]`
  - `CONDITIONAL_JUMP` [`00bc7c98`](#insn-00bc7c98) → [`00bc7cc4`](#insn-00bc7cc4)
  - `FALL_THROUGH` [`00bc7c98`](#insn-00bc7c98) → [`00bc7c9c`](#insn-00bc7c9c)
- ブロック [`00bc7c9c`](#insn-00bc7c9c) 範囲 `[['00bc7c9c', '00bc7cbb']]`
  - `CONDITIONAL_JUMP` [`00bc7cb8`](#insn-00bc7cb8) → [`00bc7f18`](#insn-00bc7f18)
  - `FALL_THROUGH` [`00bc7cb8`](#insn-00bc7cb8) → [`00bc7cbc`](#insn-00bc7cbc)
- ブロック [`00bc7cbc`](#insn-00bc7cbc) 範囲 `[['00bc7cbc', '00bc7cc3']]`
  - `FALL_THROUGH` [`00bc7cc0`](#insn-00bc7cc0) → [`00bc7cc4`](#insn-00bc7cc4)
- ブロック [`00bc7cc4`](#insn-00bc7cc4) 範囲 `[['00bc7cc4', '00bc7cdb']]`
  - `FALL_THROUGH` [`00bc7cd8`](#insn-00bc7cd8) → [`00bc7cdc`](#insn-00bc7cdc)
- ブロック [`00bc7cdc`](#insn-00bc7cdc) 範囲 `[['00bc7cdc', '00bc7cf3']]`
  - `CONDITIONAL_JUMP` [`00bc7cf0`](#insn-00bc7cf0) → [`00bc7d08`](#insn-00bc7d08)
  - `FALL_THROUGH` [`00bc7cf0`](#insn-00bc7cf0) → [`00bc7cf4`](#insn-00bc7cf4)
- ブロック [`00bc7cf4`](#insn-00bc7cf4) 範囲 `[['00bc7cf4', '00bc7cf7']]`
  - `FALL_THROUGH` [`00bc7cf4`](#insn-00bc7cf4) → [`00bc7cf8`](#insn-00bc7cf8)
- ブロック [`00bc7cf8`](#insn-00bc7cf8) 範囲 `[['00bc7cf8', '00bc7d07']]`
  - `FALL_THROUGH` [`00bc7d04`](#insn-00bc7d04) → [`00bc7d08`](#insn-00bc7d08)
- ブロック [`00bc7d08`](#insn-00bc7d08) 範囲 `[['00bc7d08', '00bc7d13']]`
  - `FALL_THROUGH` [`00bc7d10`](#insn-00bc7d10) → [`00bc7d14`](#insn-00bc7d14)
- ブロック [`00bc7d14`](#insn-00bc7d14) 範囲 `[['00bc7d14', '00bc7d27']]`
  - `CONDITIONAL_JUMP` [`00bc7d24`](#insn-00bc7d24) → [`00bc7d50`](#insn-00bc7d50)
  - `FALL_THROUGH` [`00bc7d24`](#insn-00bc7d24) → [`00bc7d28`](#insn-00bc7d28)
- ブロック [`00bc7d28`](#insn-00bc7d28) 範囲 `[['00bc7d28', '00bc7d2f']]`
  - `FALL_THROUGH` [`00bc7d2c`](#insn-00bc7d2c) → [`00bc7d30`](#insn-00bc7d30)
- ブロック [`00bc7d30`](#insn-00bc7d30) 範囲 `[['00bc7d30', '00bc7d47']]`
  - `CONDITIONAL_JUMP` [`00bc7d44`](#insn-00bc7d44) → [`00bc7f1c`](#insn-00bc7f1c)
  - `FALL_THROUGH` [`00bc7d44`](#insn-00bc7d44) → [`00bc7d48`](#insn-00bc7d48)
- ブロック [`00bc7d48`](#insn-00bc7d48) 範囲 `[['00bc7d48', '00bc7d4b']]`
  - `FALL_THROUGH` [`00bc7d48`](#insn-00bc7d48) → [`00bc7d4c`](#insn-00bc7d4c)
- ブロック [`00bc7d4c`](#insn-00bc7d4c) 範囲 `[['00bc7d4c', '00bc7d4f']]`
  - `FALL_THROUGH` [`00bc7d4c`](#insn-00bc7d4c) → [`00bc7d50`](#insn-00bc7d50)
- ブロック [`00bc7d50`](#insn-00bc7d50) 範囲 `[['00bc7d50', '00bc7d63']]`
  - `CONDITIONAL_JUMP` [`00bc7d60`](#insn-00bc7d60) → [`00bc7dbc`](#insn-00bc7dbc)
  - `FALL_THROUGH` [`00bc7d60`](#insn-00bc7d60) → [`00bc7d64`](#insn-00bc7d64)
- ブロック [`00bc7d64`](#insn-00bc7d64) 範囲 `[['00bc7d64', '00bc7d67']]`
  - `FALL_THROUGH` [`00bc7d64`](#insn-00bc7d64) → [`00bc7d68`](#insn-00bc7d68)
- ブロック [`00bc7d68`](#insn-00bc7d68) 範囲 `[['00bc7d68', '00bc7d7b']]`
  - `CONDITIONAL_JUMP` [`00bc7d78`](#insn-00bc7d78) → [`00bc7da0`](#insn-00bc7da0)
  - `FALL_THROUGH` [`00bc7d78`](#insn-00bc7d78) → [`00bc7d7c`](#insn-00bc7d7c)
- ブロック [`00bc7d7c`](#insn-00bc7d7c) 範囲 `[['00bc7d7c', '00bc7d83']]`
  - `FALL_THROUGH` [`00bc7d80`](#insn-00bc7d80) → [`00bc7d84`](#insn-00bc7d84)
- ブロック [`00bc7d84`](#insn-00bc7d84) 範囲 `[['00bc7d84', '00bc7d9b']]`
  - `CONDITIONAL_JUMP` [`00bc7d98`](#insn-00bc7d98) → [`00bc7f14`](#insn-00bc7f14)
  - `FALL_THROUGH` [`00bc7d98`](#insn-00bc7d98) → [`00bc7d9c`](#insn-00bc7d9c)
- ブロック [`00bc7d9c`](#insn-00bc7d9c) 範囲 `[['00bc7d9c', '00bc7d9f']]`
  - `FALL_THROUGH` [`00bc7d9c`](#insn-00bc7d9c) → [`00bc7da0`](#insn-00bc7da0)
- ブロック [`00bc7da0`](#insn-00bc7da0) 範囲 `[['00bc7da0', '00bc7db3']]`
  - `FALL_THROUGH` [`00bc7db0`](#insn-00bc7db0) → [`00bc7db4`](#insn-00bc7db4)
- ブロック [`00bc7db4`](#insn-00bc7db4) 範囲 `[['00bc7db4', '00bc7dbb']]`
  - `FALL_THROUGH` [`00bc7db8`](#insn-00bc7db8) → [`00bc7dbc`](#insn-00bc7dbc)
- ブロック [`00bc7dbc`](#insn-00bc7dbc) 範囲 `[['00bc7dbc', '00bc7dcb']]`
  - `FALL_THROUGH` [`00bc7dc8`](#insn-00bc7dc8) → [`00bc7dcc`](#insn-00bc7dcc)
- ブロック [`00bc7dcc`](#insn-00bc7dcc) 範囲 `[['00bc7dcc', '00bc7dd7']]`
  - `CONDITIONAL_JUMP` [`00bc7dd4`](#insn-00bc7dd4) → [`00bc7e20`](#insn-00bc7e20)
  - `FALL_THROUGH` [`00bc7dd4`](#insn-00bc7dd4) → [`00bc7dd8`](#insn-00bc7dd8)
- ブロック [`00bc7dd8`](#insn-00bc7dd8) 範囲 `[['00bc7dd8', '00bc7de3']]`
  - `FALL_THROUGH` [`00bc7de0`](#insn-00bc7de0) → [`00bc7de4`](#insn-00bc7de4)
- ブロック [`00bc7de4`](#insn-00bc7de4) 範囲 `[['00bc7de4', '00bc7dfb']]`
  - `CONDITIONAL_JUMP` [`00bc7df8`](#insn-00bc7df8) → [`00bc7f00`](#insn-00bc7f00)
  - `FALL_THROUGH` [`00bc7df8`](#insn-00bc7df8) → [`00bc7dfc`](#insn-00bc7dfc)
- ブロック [`00bc7dfc`](#insn-00bc7dfc) 範囲 `[['00bc7dfc', '00bc7e13']]`
  - `FALL_THROUGH` [`00bc7e10`](#insn-00bc7e10) → [`00bc7e14`](#insn-00bc7e14)
- ブロック [`00bc7e14`](#insn-00bc7e14) 範囲 `[['00bc7e14', '00bc7e1f']]`
- ブロック [`00bc7e20`](#insn-00bc7e20) 範囲 `[['00bc7e20', '00bc7e2b']]`
  - `FALL_THROUGH` [`00bc7e28`](#insn-00bc7e28) → [`00bc7e2c`](#insn-00bc7e2c)
- ブロック [`00bc7e2c`](#insn-00bc7e2c) 範囲 `[['00bc7e2c', '00bc7e3f']]`
  - `CONDITIONAL_JUMP` [`00bc7e3c`](#insn-00bc7e3c) → [`00bc7e68`](#insn-00bc7e68)
  - `FALL_THROUGH` [`00bc7e3c`](#insn-00bc7e3c) → [`00bc7e40`](#insn-00bc7e40)
- ブロック [`00bc7e40`](#insn-00bc7e40) 範囲 `[['00bc7e40', '00bc7e47']]`
  - `FALL_THROUGH` [`00bc7e44`](#insn-00bc7e44) → [`00bc7e48`](#insn-00bc7e48)
- ブロック [`00bc7e48`](#insn-00bc7e48) 範囲 `[['00bc7e48', '00bc7e5f']]`
  - `CONDITIONAL_JUMP` [`00bc7e5c`](#insn-00bc7e5c) → [`00bc7f20`](#insn-00bc7f20)
  - `FALL_THROUGH` [`00bc7e5c`](#insn-00bc7e5c) → [`00bc7e60`](#insn-00bc7e60)
- ブロック [`00bc7e60`](#insn-00bc7e60) 範囲 `[['00bc7e60', '00bc7e63']]`
  - `FALL_THROUGH` [`00bc7e60`](#insn-00bc7e60) → [`00bc7e64`](#insn-00bc7e64)
- ブロック [`00bc7e64`](#insn-00bc7e64) 範囲 `[['00bc7e64', '00bc7e67']]`
  - `FALL_THROUGH` [`00bc7e64`](#insn-00bc7e64) → [`00bc7e68`](#insn-00bc7e68)
- ブロック [`00bc7e68`](#insn-00bc7e68) 範囲 `[['00bc7e68', '00bc7e7f']]`
  - `FALL_THROUGH` [`00bc7e7c`](#insn-00bc7e7c) → [`00bc7e80`](#insn-00bc7e80)
- ブロック [`00bc7e80`](#insn-00bc7e80) 範囲 `[['00bc7e80', '00bc7e97']]`
  - `CONDITIONAL_JUMP` [`00bc7e94`](#insn-00bc7e94) → [`00bc7eac`](#insn-00bc7eac)
  - `FALL_THROUGH` [`00bc7e94`](#insn-00bc7e94) → [`00bc7e98`](#insn-00bc7e98)
- ブロック [`00bc7e98`](#insn-00bc7e98) 範囲 `[['00bc7e98', '00bc7e9b']]`
  - `FALL_THROUGH` [`00bc7e98`](#insn-00bc7e98) → [`00bc7e9c`](#insn-00bc7e9c)
- ブロック [`00bc7e9c`](#insn-00bc7e9c) 範囲 `[['00bc7e9c', '00bc7eab']]`
  - `FALL_THROUGH` [`00bc7ea8`](#insn-00bc7ea8) → [`00bc7eac`](#insn-00bc7eac)
- ブロック [`00bc7eac`](#insn-00bc7eac) 範囲 `[['00bc7eac', '00bc7eb3']]`
  - `FALL_THROUGH` [`00bc7eb0`](#insn-00bc7eb0) → [`00bc7eb4`](#insn-00bc7eb4)
- ブロック [`00bc7eb4`](#insn-00bc7eb4) 範囲 `[['00bc7eb4', '00bc7ecb']]`
  - `CONDITIONAL_JUMP` [`00bc7ec8`](#insn-00bc7ec8) → [`00bc7ef4`](#insn-00bc7ef4)
  - `FALL_THROUGH` [`00bc7ec8`](#insn-00bc7ec8) → [`00bc7ecc`](#insn-00bc7ecc)
- ブロック [`00bc7ecc`](#insn-00bc7ecc) 範囲 `[['00bc7ecc', '00bc7ee3']]`
  - `FALL_THROUGH` [`00bc7ee0`](#insn-00bc7ee0) → [`00bc7ee4`](#insn-00bc7ee4)
- ブロック [`00bc7ee4`](#insn-00bc7ee4) 範囲 `[['00bc7ee4', '00bc7eeb']]`
  - `CONDITIONAL_JUMP` [`00bc7ee8`](#insn-00bc7ee8) → [`00bc7f24`](#insn-00bc7f24)
  - `FALL_THROUGH` [`00bc7ee8`](#insn-00bc7ee8) → [`00bc7eec`](#insn-00bc7eec)
- ブロック [`00bc7eec`](#insn-00bc7eec) 範囲 `[['00bc7eec', '00bc7ef3']]`
  - `FALL_THROUGH` [`00bc7ef0`](#insn-00bc7ef0) → [`00bc7ef4`](#insn-00bc7ef4)
- ブロック [`00bc7ef4`](#insn-00bc7ef4) 範囲 `[['00bc7ef4', '00bc7efb']]`
  - `FALL_THROUGH` [`00bc7ef8`](#insn-00bc7ef8) → [`00bc7efc`](#insn-00bc7efc)
- ブロック [`00bc7efc`](#insn-00bc7efc) 範囲 `[['00bc7efc', '00bc7eff']]`
  - `FALL_THROUGH` [`00bc7efc`](#insn-00bc7efc) → [`00bc7f00`](#insn-00bc7f00)
- ブロック [`00bc7f00`](#insn-00bc7f00) 範囲 `[['00bc7f00', '00bc7f13']]`
- ブロック [`00bc7f14`](#insn-00bc7f14) 範囲 `[['00bc7f14', '00bc7f17']]`
- ブロック [`00bc7f18`](#insn-00bc7f18) 範囲 `[['00bc7f18', '00bc7f1b']]`
- ブロック [`00bc7f1c`](#insn-00bc7f1c) 範囲 `[['00bc7f1c', '00bc7f1f']]`
- ブロック [`00bc7f20`](#insn-00bc7f20) 範囲 `[['00bc7f20', '00bc7f23']]`
- ブロック [`00bc7f24`](#insn-00bc7f24) 範囲 `[['00bc7f24', '00bc7f27']]`

## 命令位置別の参照

- [`00bc7c00`](#insn-00bc7c00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7c04`](#insn-00bc7c04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7c08`](#insn-00bc7c08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7c34`](#insn-00bc7c34) → [`00bc7c7c`](#insn-00bc7c7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7c58`](#insn-00bc7c58) → [`00bc7c70`](#insn-00bc7c70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7c74`](#insn-00bc7c74) → [`00bc7d64`](#insn-00bc7d64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7c78`](#insn-00bc7c78) → [`00bc7dbc`](#insn-00bc7dbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7c98`](#insn-00bc7c98) → [`00bc7cc4`](#insn-00bc7cc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7cb0`](#insn-00bc7cb0) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bc7cb8`](#insn-00bc7cb8) → [`00bc7f18`](#insn-00bc7f18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7cf0`](#insn-00bc7cf0) → [`00bc7d08`](#insn-00bc7d08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7d24`](#insn-00bc7d24) → [`00bc7d50`](#insn-00bc7d50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7d3c`](#insn-00bc7d3c) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bc7d44`](#insn-00bc7d44) → [`00bc7f1c`](#insn-00bc7f1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7d60`](#insn-00bc7d60) → [`00bc7dbc`](#insn-00bc7dbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7d78`](#insn-00bc7d78) → [`00bc7da0`](#insn-00bc7da0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7d90`](#insn-00bc7d90) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bc7d98`](#insn-00bc7d98) → [`00bc7f14`](#insn-00bc7f14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7dac`](#insn-00bc7dac) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00bc7dd4`](#insn-00bc7dd4) → [`00bc7e20`](#insn-00bc7e20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7df8`](#insn-00bc7df8) → [`00bc7f00`](#insn-00bc7f00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e0c`](#insn-00bc7e0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e10`](#insn-00bc7e10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e14`](#insn-00bc7e14) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e3c`](#insn-00bc7e3c) → [`00bc7e68`](#insn-00bc7e68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e54`](#insn-00bc7e54) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e5c`](#insn-00bc7e5c) → [`00bc7f20`](#insn-00bc7f20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e94`](#insn-00bc7e94) → [`00bc7eac`](#insn-00bc7eac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7ec8`](#insn-00bc7ec8) → [`00bc7ef4`](#insn-00bc7ef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7ee0`](#insn-00bc7ee0) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bc7ee8`](#insn-00bc7ee8) → [`00bc7f24`](#insn-00bc7f24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f00`](#insn-00bc7f00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f04`](#insn-00bc7f04) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f08`](#insn-00bc7f08) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f14`](#insn-00bc7f14) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f18`](#insn-00bc7f18) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f1c`](#insn-00bc7f1c) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f20`](#insn-00bc7f20) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f24`](#insn-00bc7f24) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc7c00`](#insn-00bc7c00)

~~~json
{
  "source": "00bc7c00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7c04`](#insn-00bc7c04)

~~~json
{
  "source": "00bc7c04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7c08`](#insn-00bc7c08)

~~~json
{
  "source": "00bc7c08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7c34`](#insn-00bc7c34)

~~~json
{
  "source": "00bc7c34",
  "target": "00bc7c7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7c58`](#insn-00bc7c58)

~~~json
{
  "source": "00bc7c58",
  "target": "00bc7c70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7c74`](#insn-00bc7c74)

~~~json
{
  "source": "00bc7c74",
  "target": "00bc7d64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7c78`](#insn-00bc7c78)

~~~json
{
  "source": "00bc7c78",
  "target": "00bc7dbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7c98`](#insn-00bc7c98)

~~~json
{
  "source": "00bc7c98",
  "target": "00bc7cc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7cb0`](#insn-00bc7cb0)

~~~json
{
  "source": "00bc7cb0",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7cb8`](#insn-00bc7cb8)

~~~json
{
  "source": "00bc7cb8",
  "target": "00bc7f18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7cf0`](#insn-00bc7cf0)

~~~json
{
  "source": "00bc7cf0",
  "target": "00bc7d08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7d24`](#insn-00bc7d24)

~~~json
{
  "source": "00bc7d24",
  "target": "00bc7d50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7d3c`](#insn-00bc7d3c)

~~~json
{
  "source": "00bc7d3c",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7d44`](#insn-00bc7d44)

~~~json
{
  "source": "00bc7d44",
  "target": "00bc7f1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7d60`](#insn-00bc7d60)

~~~json
{
  "source": "00bc7d60",
  "target": "00bc7dbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7d78`](#insn-00bc7d78)

~~~json
{
  "source": "00bc7d78",
  "target": "00bc7da0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7d90`](#insn-00bc7d90)

~~~json
{
  "source": "00bc7d90",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7d98`](#insn-00bc7d98)

~~~json
{
  "source": "00bc7d98",
  "target": "00bc7f14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7dac`](#insn-00bc7dac)

~~~json
{
  "source": "00bc7dac",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7dd4`](#insn-00bc7dd4)

~~~json
{
  "source": "00bc7dd4",
  "target": "00bc7e20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7df8`](#insn-00bc7df8)

~~~json
{
  "source": "00bc7df8",
  "target": "00bc7f00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7e0c`](#insn-00bc7e0c)

~~~json
{
  "source": "00bc7e0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7e10`](#insn-00bc7e10)

~~~json
{
  "source": "00bc7e10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7e14`](#insn-00bc7e14)

~~~json
{
  "source": "00bc7e14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7e3c`](#insn-00bc7e3c)

~~~json
{
  "source": "00bc7e3c",
  "target": "00bc7e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7e54`](#insn-00bc7e54)

~~~json
{
  "source": "00bc7e54",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7e5c`](#insn-00bc7e5c)

~~~json
{
  "source": "00bc7e5c",
  "target": "00bc7f20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7e94`](#insn-00bc7e94)

~~~json
{
  "source": "00bc7e94",
  "target": "00bc7eac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7ec8`](#insn-00bc7ec8)

~~~json
{
  "source": "00bc7ec8",
  "target": "00bc7ef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7ee0`](#insn-00bc7ee0)

~~~json
{
  "source": "00bc7ee0",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7ee8`](#insn-00bc7ee8)

~~~json
{
  "source": "00bc7ee8",
  "target": "00bc7f24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f00`](#insn-00bc7f00)

~~~json
{
  "source": "00bc7f00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f04`](#insn-00bc7f04)

~~~json
{
  "source": "00bc7f04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f08`](#insn-00bc7f08)

~~~json
{
  "source": "00bc7f08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f14`](#insn-00bc7f14)

~~~json
{
  "source": "00bc7f14",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7f18`](#insn-00bc7f18)

~~~json
{
  "source": "00bc7f18",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7f1c`](#insn-00bc7f1c)

~~~json
{
  "source": "00bc7f1c",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7f20`](#insn-00bc7f20)

~~~json
{
  "source": "00bc7f20",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7f24`](#insn-00bc7f24)

~~~json
{
  "source": "00bc7f24",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
