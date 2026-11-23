# 00bcfe1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bcfd54`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfd54.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-27a2eeb42f7c3f2d99a55110b41f3a74)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bcfe60`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfe60.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-68f16932f4016f9a81e810bc0f35f033)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfe1c",
  "name": "FUN_00bcfe1c",
  "size": 256,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c0fb4a399350135fab51fb3637df072a90c8159fc6c94e6a3f4804a75f136bf7",
  "source_text_sha256": "c0fb4a399350135fab51fb3637df072a90c8159fc6c94e6a3f4804a75f136bf7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfe1c",
        "00bcff1b"
      ]
    ],
    "bytes_sha256": "2b42fe660c9fbc0f602a76c01f60b86f2dd0fd0670a505aecfc31d6c3cdc65e0",
    "instruction_count": 64,
    "instruction_bytes": 256,
    "body_bytes": 256,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1829 bytes

~~~c

void FUN_00bcfe1c(long param_1,undefined8 *param_2)

{
  void *__ptr;
  long lVar1;
  size_t __size;
  ulong uVar2;
  long *plVar3;
  
  plVar3 = *(long **)(param_1 + 0x18);
  (**(code **)(*plVar3 + 0x20))(plVar3);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  }
  lVar1 = param_2[1];
                    /* try { // try from 00bcfe74 to 00ccfe7b has its CatchHandler @ 00bcff0c */
  __ptr = (void *)*param_2;
  uVar2 = lVar1 + 1;
                    /* try { // try from 00bcfe7c to 00ccfea7 has its CatchHandler @ 00bcfe1c */
  if ((ulong)param_2[2] < uVar2) {
    __size = param_2[2] * 2;
    uVar2 = lVar1 + 0x3e1;
    if (__size < uVar2 || __size - uVar2 == 0) {
      __size = uVar2;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar1 = param_2[1];
                    /* try { // try from 00bcfea8 to 00ccfec3 has its CatchHandler @ 00bcff14 */
    uVar2 = lVar1 + 1;
  }
  param_2[1] = uVar2;
  *(undefined1 *)((long)__ptr + lVar1) = 0x40;
  plVar3 = *(long **)(param_1 + 0x10);
                    /* try { // try from 00bcfec4 to 00ccff53 has its CatchHandler @ 00bcfe1c */
  (**(code **)(*plVar3 + 0x20))(plVar3,param_2);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* catch() { ... } // from try @ 00bcfe74 with catch @ 00bcff0c */
                    /* WARNING: Could not recover jumptable at 0x00bcff14. Too many branches */
                    /* WARNING: Treating indirect jump as call */
                    /* catch() { ... } // from try @ 00bcfea8 with catch @ 00bcff14 */
  (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcfe1c"></a> `00bcfe1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcfe20"></a> `00bcfe20` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcfe24"></a> `00bcfe24` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfe28"></a> `00bcfe28` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfe2c"></a> `00bcfe2c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcfe30"></a> `00bcfe30` | `15 0c 40 f9` | ldr x21,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bcfe34"></a> `00bcfe34` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcfe38"></a> `00bcfe38` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcfe3c"></a> `00bcfe3c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcfe40"></a> `00bcfe40` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcfe44"></a> `00bcfe44` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfe48"></a> `00bcfe48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfe4c"></a> `00bcfe4c` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bcfe50"></a> `00bcfe50` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcfe54"></a> `00bcfe54` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcfe58"></a> `00bcfe58` | `c0 00 00 54` | b.eq 0x00bcfe70 | `CONDITIONAL_JUMP`
<a id="insn-00bcfe5c"></a> `00bcfe5c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcfe60"></a> `00bcfe60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcfe64"></a> `00bcfe64` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcfe68"></a> `00bcfe68` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfe6c"></a> `00bcfe6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfe70"></a> `00bcfe70` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfe74"></a> `00bcfe74` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcfe78"></a> `00bcfe78` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfe7c"></a> `00bcfe7c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcfe80"></a> `00bcfe80` | `69 01 00 54` | b.ls 0x00bcfeac | `CONDITIONAL_JUMP`
<a id="insn-00bcfe84"></a> `00bcfe84` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfe88"></a> `00bcfe88` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcfe8c"></a> `00bcfe8c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcfe90"></a> `00bcfe90` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcfe94"></a> `00bcfe94` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfe98"></a> `00bcfe98` | `da 34 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe9c"></a> `00bcfe9c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcfea0"></a> `00bcfea0` | `c0 03 00 b4` | cbz x0,0x00bcff18 | `CONDITIONAL_JUMP`
<a id="insn-00bcfea4"></a> `00bcfea4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfea8"></a> `00bcfea8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfeac"></a> `00bcfeac` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfeb0"></a> `00bcfeb0` | `09 08 80 52` | mov w9,#0x40 | `FALL_THROUGH`
<a id="insn-00bcfeb4"></a> `00bcfeb4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcfeb8"></a> `00bcfeb8` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcfebc"></a> `00bcfebc` | `94 0a 40 f9` | ldr x20,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfec0"></a> `00bcfec0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcfec4"></a> `00bcfec4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcfec8"></a> `00bcfec8` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfecc"></a> `00bcfecc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfed0"></a> `00bcfed0` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bcfed4"></a> `00bcfed4` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcfed8"></a> `00bcfed8` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcfedc"></a> `00bcfedc` | `c1 00 00 54` | b.ne 0x00bcfef4 | `CONDITIONAL_JUMP`
<a id="insn-00bcfee0"></a> `00bcfee0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfee4"></a> `00bcfee4` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfee8"></a> `00bcfee8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcfeec"></a> `00bcfeec` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcfef0"></a> `00bcfef0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcfef4"></a> `00bcfef4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcfef8"></a> `00bcfef8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcfefc"></a> `00bcfefc` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcff00"></a> `00bcff00` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcff04"></a> `00bcff04` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcff08"></a> `00bcff08` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcff0c"></a> `00bcff0c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcff10"></a> `00bcff10` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcff14"></a> `00bcff14` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bcff18"></a> `00bcff18` | `d6 38 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfe1c`](#insn-00bcfe1c) 範囲 `[['00bcfe1c', '00bcfe5b']]`
  - `CONDITIONAL_JUMP` [`00bcfe58`](#insn-00bcfe58) → [`00bcfe70`](#insn-00bcfe70)
  - `FALL_THROUGH` [`00bcfe58`](#insn-00bcfe58) → [`00bcfe5c`](#insn-00bcfe5c)
- ブロック [`00bcfe5c`](#insn-00bcfe5c) 範囲 `[['00bcfe5c', '00bcfe6f']]`
  - `FALL_THROUGH` [`00bcfe6c`](#insn-00bcfe6c) → [`00bcfe70`](#insn-00bcfe70)
- ブロック [`00bcfe70`](#insn-00bcfe70) 範囲 `[['00bcfe70', '00bcfe73']]`
  - `FALL_THROUGH` [`00bcfe70`](#insn-00bcfe70) → [`00bcfe74`](#insn-00bcfe74)
- ブロック [`00bcfe74`](#insn-00bcfe74) 範囲 `[['00bcfe74', '00bcfe7b']]`
  - `FALL_THROUGH` [`00bcfe78`](#insn-00bcfe78) → [`00bcfe7c`](#insn-00bcfe7c)
- ブロック [`00bcfe7c`](#insn-00bcfe7c) 範囲 `[['00bcfe7c', '00bcfe83']]`
  - `CONDITIONAL_JUMP` [`00bcfe80`](#insn-00bcfe80) → [`00bcfeac`](#insn-00bcfeac)
  - `FALL_THROUGH` [`00bcfe80`](#insn-00bcfe80) → [`00bcfe84`](#insn-00bcfe84)
- ブロック [`00bcfe84`](#insn-00bcfe84) 範囲 `[['00bcfe84', '00bcfea3']]`
  - `CONDITIONAL_JUMP` [`00bcfea0`](#insn-00bcfea0) → [`00bcff18`](#insn-00bcff18)
  - `FALL_THROUGH` [`00bcfea0`](#insn-00bcfea0) → [`00bcfea4`](#insn-00bcfea4)
- ブロック [`00bcfea4`](#insn-00bcfea4) 範囲 `[['00bcfea4', '00bcfea7']]`
  - `FALL_THROUGH` [`00bcfea4`](#insn-00bcfea4) → [`00bcfea8`](#insn-00bcfea8)
- ブロック [`00bcfea8`](#insn-00bcfea8) 範囲 `[['00bcfea8', '00bcfeab']]`
  - `FALL_THROUGH` [`00bcfea8`](#insn-00bcfea8) → [`00bcfeac`](#insn-00bcfeac)
- ブロック [`00bcfeac`](#insn-00bcfeac) 範囲 `[['00bcfeac', '00bcfec3']]`
  - `FALL_THROUGH` [`00bcfec0`](#insn-00bcfec0) → [`00bcfec4`](#insn-00bcfec4)
- ブロック [`00bcfec4`](#insn-00bcfec4) 範囲 `[['00bcfec4', '00bcfedf']]`
  - `CONDITIONAL_JUMP` [`00bcfedc`](#insn-00bcfedc) → [`00bcfef4`](#insn-00bcfef4)
  - `FALL_THROUGH` [`00bcfedc`](#insn-00bcfedc) → [`00bcfee0`](#insn-00bcfee0)
- ブロック [`00bcfee0`](#insn-00bcfee0) 範囲 `[['00bcfee0', '00bcfef3']]`
- ブロック [`00bcfef4`](#insn-00bcfef4) 範囲 `[['00bcfef4', '00bcff0b']]`
  - `FALL_THROUGH` [`00bcff08`](#insn-00bcff08) → [`00bcff0c`](#insn-00bcff0c)
- ブロック [`00bcff0c`](#insn-00bcff0c) 範囲 `[['00bcff0c', '00bcff13']]`
  - `FALL_THROUGH` [`00bcff10`](#insn-00bcff10) → [`00bcff14`](#insn-00bcff14)
- ブロック [`00bcff14`](#insn-00bcff14) 範囲 `[['00bcff14', '00bcff17']]`
- ブロック [`00bcff18`](#insn-00bcff18) 範囲 `[['00bcff18', '00bcff1b']]`

## 命令位置別の参照

- [`00bcfe20`](#insn-00bcfe20) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe24`](#insn-00bcfe24) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe28`](#insn-00bcfe28) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe58`](#insn-00bcfe58) → [`00bcfe70`](#insn-00bcfe70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe80`](#insn-00bcfe80) → [`00bcfeac`](#insn-00bcfeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe98`](#insn-00bcfe98) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcfea0`](#insn-00bcfea0) → [`00bcff18`](#insn-00bcff18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfedc`](#insn-00bcfedc) → [`00bcfef4`](#insn-00bcfef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfee0`](#insn-00bcfee0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfee4`](#insn-00bcfee4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfee8`](#insn-00bcfee8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff04`](#insn-00bcff04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff08`](#insn-00bcff08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff0c`](#insn-00bcff0c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff18`](#insn-00bcff18) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfe20`](#insn-00bcfe20)

~~~json
{
  "source": "00bcfe20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe24`](#insn-00bcfe24)

~~~json
{
  "source": "00bcfe24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe28`](#insn-00bcfe28)

~~~json
{
  "source": "00bcfe28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe58`](#insn-00bcfe58)

~~~json
{
  "source": "00bcfe58",
  "target": "00bcfe70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe80`](#insn-00bcfe80)

~~~json
{
  "source": "00bcfe80",
  "target": "00bcfeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe98`](#insn-00bcfe98)

~~~json
{
  "source": "00bcfe98",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfea0`](#insn-00bcfea0)

~~~json
{
  "source": "00bcfea0",
  "target": "00bcff18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfedc`](#insn-00bcfedc)

~~~json
{
  "source": "00bcfedc",
  "target": "00bcfef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfee0`](#insn-00bcfee0)

~~~json
{
  "source": "00bcfee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfee4`](#insn-00bcfee4)

~~~json
{
  "source": "00bcfee4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfee8`](#insn-00bcfee8)

~~~json
{
  "source": "00bcfee8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff04`](#insn-00bcff04)

~~~json
{
  "source": "00bcff04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff08`](#insn-00bcff08)

~~~json
{
  "source": "00bcff08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff0c`](#insn-00bcff0c)

~~~json
{
  "source": "00bcff0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff18`](#insn-00bcff18)

~~~json
{
  "source": "00bcff18",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
