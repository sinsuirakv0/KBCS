# 00bb9bac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bb9c74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9c74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-d7b682666c200d49aed26ed26dccfe1d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb9bac",
  "name": "FUN_00bb9bac",
  "size": 268,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83fecfcac7ee0604b7fc2bbf32aeb8dbe6b31b45d98b6e36bdca53bdb0706aff",
  "source_text_sha256": "83fecfcac7ee0604b7fc2bbf32aeb8dbe6b31b45d98b6e36bdca53bdb0706aff",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb9bac",
        "00bb9cb7"
      ]
    ],
    "bytes_sha256": "3c741aa168f42cb9bfc438e195027d8946125a762059f211e91de9adac0c0730",
    "instruction_count": 67,
    "instruction_bytes": 268,
    "body_bytes": 268,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b8d1a8](../00b8d/00b8d1a8.md)
- [00b90628](../00b90/00b90628.md)

## 呼び出し先

- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)
- [00bdb170](../00bdb/00bdb170.md)
- [00be1470](../00be1/00be1470.md)
- [00be1ca0](../00be1/00be1ca0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1290 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

double FUN_00bb9bac(char *param_1,char *param_2,undefined4 *param_3)

{
  int iVar1;
  int iVar2;
  int *piVar3;
  double dVar4;
  double dVar5;
  char *local_48;
  
  dVar5 = _DAT_002b1870;
  if (param_1 == param_2) {
                    /* try { // try from 00bb9c34 to 00cb9ca7 has its CatchHandler @ 00bbad98 */
    *param_3 = 4;
  }
  else {
    piVar3 = (int *)__errno();
    iVar1 = *piVar3;
    *piVar3 = 0;
                    /* try { // try from 00bb9be8 to 00cb9bfb has its CatchHandler @ 00bbaaf0 */
    if (((DAT_010a2898 & 1) == 0) && (iVar2 = __cxa_guard_acquire(&DAT_010a2898), iVar2 != 0)) {
      DAT_010a2890 = newlocale(0x1fbf,"C",(__locale_t)0x0);
      __cxa_guard_release(&DAT_010a2898);
    }
    dVar4 = strtold_l(param_1,&local_48,DAT_010a2890);
    if (*piVar3 == 0) {
      *piVar3 = iVar1;
      dVar5 = _DAT_002b1870;
      if (local_48 == param_2) {
        return dVar4;
      }
    }
    else {
      dVar5 = _DAT_002b1870;
                    /* try { // try from 00bb9c28 to 00cb9c33 has its CatchHandler @ 00bbad64 */
      if ((local_48 == param_2) && (dVar5 = dVar4, *piVar3 != 0x22)) {
        return dVar4;
      }
    }
    *param_3 = 4;
  }
  return dVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb9bac"></a> `00bb9bac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bb9bb0"></a> `00bb9bb0` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bb9bb4"></a> `00bb9bb4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb9bb8"></a> `00bb9bb8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb9bbc"></a> `00bb9bbc` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb9bc0"></a> `00bb9bc0` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb9bc4"></a> `00bb9bc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bb9bc8"></a> `00bb9bc8` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bb9bcc"></a> `00bb9bcc` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bb9bd0"></a> `00bb9bd0` | `00 03 00 54` | b.eq 0x00bb9c30 | `CONDITIONAL_JUMP`
<a id="insn-00bb9bd4"></a> `00bb9bd4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bb9bd8"></a> `00bb9bd8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bb9bdc"></a> `00bb9bdc` | `65 85 00 94` | bl 0x00bdb170 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9be0"></a> `00bb9be0` | `17 00 40 b9` | ldr w23,[x0] | `FALL_THROUGH`
<a id="insn-00bb9be4"></a> `00bb9be4` | `1f 00 00 b9` | str wzr,[x0] | `FALL_THROUGH`
<a id="insn-00bb9be8"></a> `00bb9be8` | `48 27 00 b0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb9bec"></a> `00bb9bec` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bb9bf0"></a> `00bb9bf0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bb9bf4"></a> `00bb9bf4` | `58 27 00 b0` | adrp x24,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb9bf8"></a> `00bb9bf8` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bb9bfc"></a> `00bb9bfc` | `28 04 00 36` | tbz w8,#0x0,0x00bb9c80 | `CONDITIONAL_JUMP`
<a id="insn-00bb9c00"></a> `00bb9c00` | `02 4b 44 f9` | ldr x2,[x24, #0x890] | `FALL_THROUGH`
<a id="insn-00bb9c04"></a> `00bb9c04` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bb9c08"></a> `00bb9c08` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bb9c0c"></a> `00bb9c0c` | `25 a0 00 94` | bl 0x00be1ca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9c10"></a> `00bb9c10` | `a8 02 40 b9` | ldr w8,[x21] | `FALL_THROUGH`
<a id="insn-00bb9c14"></a> `00bb9c14` | `88 01 00 34` | cbz w8,0x00bb9c44 | `CONDITIONAL_JUMP`
<a id="insn-00bb9c18"></a> `00bb9c18` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bb9c1c"></a> `00bb9c1c` | `3f 01 14 eb` | cmp x9,x20 | `FALL_THROUGH`
<a id="insn-00bb9c20"></a> `00bb9c20` | `a1 01 00 54` | b.ne 0x00bb9c54 | `CONDITIONAL_JUMP`
<a id="insn-00bb9c24"></a> `00bb9c24` | `1f 89 00 71` | cmp w8,#0x22 | `FALL_THROUGH`
<a id="insn-00bb9c28"></a> `00bb9c28` | `a0 01 00 54` | b.eq 0x00bb9c5c | `CONDITIONAL_JUMP`
<a id="insn-00bb9c2c"></a> `00bb9c2c` | `0e 00 00 14` | b 0x00bb9c64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb9c30"></a> `00bb9c30` | `c8 b7 ff 90` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00bb9c34"></a> `00bb9c34` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bb9c38"></a> `00bb9c38` | `00 1d c2 3d` | ldr q0,[x8, #0x870] | `FALL_THROUGH`
<a id="insn-00bb9c3c"></a> `00bb9c3c` | `69 02 00 b9` | str w9,[x19] | `FALL_THROUGH`
<a id="insn-00bb9c40"></a> `00bb9c40` | `09 00 00 14` | b 0x00bb9c64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb9c44"></a> `00bb9c44` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bb9c48"></a> `00bb9c48` | `b7 02 00 b9` | str w23,[x21] | `FALL_THROUGH`
<a id="insn-00bb9c4c"></a> `00bb9c4c` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00bb9c50"></a> `00bb9c50` | `a0 00 00 54` | b.eq 0x00bb9c64 | `CONDITIONAL_JUMP`
<a id="insn-00bb9c54"></a> `00bb9c54` | `c8 b7 ff 90` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00bb9c58"></a> `00bb9c58` | `00 1d c2 3d` | ldr q0,[x8, #0x870] | `FALL_THROUGH`
<a id="insn-00bb9c5c"></a> `00bb9c5c` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bb9c60"></a> `00bb9c60` | `68 02 00 b9` | str w8,[x19] | `FALL_THROUGH`
<a id="insn-00bb9c64"></a> `00bb9c64` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb9c68"></a> `00bb9c68` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb9c6c"></a> `00bb9c6c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb9c70"></a> `00bb9c70` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb9c74"></a> `00bb9c74` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bb9c78"></a> `00bb9c78` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb9c7c"></a> `00bb9c7c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bb9c80"></a> `00bb9c80` | `40 27 00 b0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb9c84"></a> `00bb9c84` | `00 60 22 91` | add x0,x0,#0x898 | `FALL_THROUGH`
<a id="insn-00bb9c88"></a> `00bb9c88` | `9e 84 00 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9c8c"></a> `00bb9c8c` | `a0 fb ff 34` | cbz w0,0x00bb9c00 | `CONDITIONAL_JUMP`
<a id="insn-00bb9c90"></a> `00bb9c90` | `61 b7 ff 90` | adrp x1,0x2a5000 | `FALL_THROUGH`
<a id="insn-00bb9c94"></a> `00bb9c94` | `21 28 1a 91` | add x1,x1,#0x68a | `FALL_THROUGH`
<a id="insn-00bb9c98"></a> `00bb9c98` | `e0 f7 83 52` | mov w0,#0x1fbf | `FALL_THROUGH`
<a id="insn-00bb9c9c"></a> `00bb9c9c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bb9ca0"></a> `00bb9ca0` | `f4 9d 00 94` | bl 0x00be1470 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9ca4"></a> `00bb9ca4` | `00 4b 04 f9` | str x0,[x24, #0x890] | `FALL_THROUGH`
<a id="insn-00bb9ca8"></a> `00bb9ca8` | `40 27 00 b0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb9cac"></a> `00bb9cac` | `00 60 22 91` | add x0,x0,#0x898 | `FALL_THROUGH`
<a id="insn-00bb9cb0"></a> `00bb9cb0` | `9c 84 00 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9cb4"></a> `00bb9cb4` | `d3 ff ff 17` | b 0x00bb9c00 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bb9bac`](#insn-00bb9bac) 範囲 `[['00bb9bac', '00bb9bd3']]`
  - `CONDITIONAL_JUMP` [`00bb9bd0`](#insn-00bb9bd0) → [`00bb9c30`](#insn-00bb9c30)
  - `FALL_THROUGH` [`00bb9bd0`](#insn-00bb9bd0) → [`00bb9bd4`](#insn-00bb9bd4)
- ブロック [`00bb9bd4`](#insn-00bb9bd4) 範囲 `[['00bb9bd4', '00bb9be7']]`
  - `FALL_THROUGH` [`00bb9be4`](#insn-00bb9be4) → [`00bb9be8`](#insn-00bb9be8)
- ブロック [`00bb9be8`](#insn-00bb9be8) 範囲 `[['00bb9be8', '00bb9bff']]`
  - `CONDITIONAL_JUMP` [`00bb9bfc`](#insn-00bb9bfc) → [`00bb9c80`](#insn-00bb9c80)
  - `FALL_THROUGH` [`00bb9bfc`](#insn-00bb9bfc) → [`00bb9c00`](#insn-00bb9c00)
- ブロック [`00bb9c00`](#insn-00bb9c00) 範囲 `[['00bb9c00', '00bb9c17']]`
  - `CONDITIONAL_JUMP` [`00bb9c14`](#insn-00bb9c14) → [`00bb9c44`](#insn-00bb9c44)
  - `FALL_THROUGH` [`00bb9c14`](#insn-00bb9c14) → [`00bb9c18`](#insn-00bb9c18)
- ブロック [`00bb9c18`](#insn-00bb9c18) 範囲 `[['00bb9c18', '00bb9c23']]`
  - `CONDITIONAL_JUMP` [`00bb9c20`](#insn-00bb9c20) → [`00bb9c54`](#insn-00bb9c54)
  - `FALL_THROUGH` [`00bb9c20`](#insn-00bb9c20) → [`00bb9c24`](#insn-00bb9c24)
- ブロック [`00bb9c24`](#insn-00bb9c24) 範囲 `[['00bb9c24', '00bb9c27']]`
  - `FALL_THROUGH` [`00bb9c24`](#insn-00bb9c24) → [`00bb9c28`](#insn-00bb9c28)
- ブロック [`00bb9c28`](#insn-00bb9c28) 範囲 `[['00bb9c28', '00bb9c2b']]`
  - `CONDITIONAL_JUMP` [`00bb9c28`](#insn-00bb9c28) → [`00bb9c5c`](#insn-00bb9c5c)
  - `FALL_THROUGH` [`00bb9c28`](#insn-00bb9c28) → [`00bb9c2c`](#insn-00bb9c2c)
- ブロック [`00bb9c2c`](#insn-00bb9c2c) 範囲 `[['00bb9c2c', '00bb9c2f']]`
  - `UNCONDITIONAL_JUMP` [`00bb9c2c`](#insn-00bb9c2c) → [`00bb9c64`](#insn-00bb9c64)
- ブロック [`00bb9c30`](#insn-00bb9c30) 範囲 `[['00bb9c30', '00bb9c33']]`
  - `FALL_THROUGH` [`00bb9c30`](#insn-00bb9c30) → [`00bb9c34`](#insn-00bb9c34)
- ブロック [`00bb9c34`](#insn-00bb9c34) 範囲 `[['00bb9c34', '00bb9c43']]`
  - `UNCONDITIONAL_JUMP` [`00bb9c40`](#insn-00bb9c40) → [`00bb9c64`](#insn-00bb9c64)
- ブロック [`00bb9c44`](#insn-00bb9c44) 範囲 `[['00bb9c44', '00bb9c53']]`
  - `CONDITIONAL_JUMP` [`00bb9c50`](#insn-00bb9c50) → [`00bb9c64`](#insn-00bb9c64)
  - `FALL_THROUGH` [`00bb9c50`](#insn-00bb9c50) → [`00bb9c54`](#insn-00bb9c54)
- ブロック [`00bb9c54`](#insn-00bb9c54) 範囲 `[['00bb9c54', '00bb9c5b']]`
  - `FALL_THROUGH` [`00bb9c58`](#insn-00bb9c58) → [`00bb9c5c`](#insn-00bb9c5c)
- ブロック [`00bb9c5c`](#insn-00bb9c5c) 範囲 `[['00bb9c5c', '00bb9c63']]`
  - `FALL_THROUGH` [`00bb9c60`](#insn-00bb9c60) → [`00bb9c64`](#insn-00bb9c64)
- ブロック [`00bb9c64`](#insn-00bb9c64) 範囲 `[['00bb9c64', '00bb9c7f']]`
- ブロック [`00bb9c80`](#insn-00bb9c80) 範囲 `[['00bb9c80', '00bb9c8f']]`
  - `CONDITIONAL_JUMP` [`00bb9c8c`](#insn-00bb9c8c) → [`00bb9c00`](#insn-00bb9c00)
  - `FALL_THROUGH` [`00bb9c8c`](#insn-00bb9c8c) → [`00bb9c90`](#insn-00bb9c90)
- ブロック [`00bb9c90`](#insn-00bb9c90) 範囲 `[['00bb9c90', '00bb9cb7']]`
  - `UNCONDITIONAL_JUMP` [`00bb9cb4`](#insn-00bb9cb4) → [`00bb9c00`](#insn-00bb9c00)

## 命令位置別の参照

- [`00bb9bb4`](#insn-00bb9bb4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9bb8`](#insn-00bb9bb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9bbc`](#insn-00bb9bbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9bc0`](#insn-00bb9bc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9bd0`](#insn-00bb9bd0) → [`00bb9c30`](#insn-00bb9c30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9bdc`](#insn-00bb9bdc) → [`00bdb170`](../00bdb/00bdb170.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb170` · 推定シンボル `None` · 推定型 `None`
- [`00bb9bf8`](#insn-00bb9bf8) → `010a2898`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb9bfc`](#insn-00bb9bfc) → [`00bb9c80`](#insn-00bb9c80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c00`](#insn-00bb9c00) → `010a2890`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb9c0c`](#insn-00bb9c0c) → [`00be1ca0`](../00be1/00be1ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1ca0` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c14`](#insn-00bb9c14) → [`00bb9c44`](#insn-00bb9c44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c18`](#insn-00bb9c18) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c20`](#insn-00bb9c20) → [`00bb9c54`](#insn-00bb9c54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c28`](#insn-00bb9c28) → [`00bb9c5c`](#insn-00bb9c5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c2c`](#insn-00bb9c2c) → [`00bb9c64`](#insn-00bb9c64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c38`](#insn-00bb9c38) → `002b1870`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c40`](#insn-00bb9c40) → [`00bb9c64`](#insn-00bb9c64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c44`](#insn-00bb9c44) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c50`](#insn-00bb9c50) → [`00bb9c64`](#insn-00bb9c64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c58`](#insn-00bb9c58) → `002b1870`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c64`](#insn-00bb9c64) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c68`](#insn-00bb9c68) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c6c`](#insn-00bb9c6c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c70`](#insn-00bb9c70) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c84`](#insn-00bb9c84) → `010a2898`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb9c88`](#insn-00bb9c88) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c8c`](#insn-00bb9c8c) → [`00bb9c00`](#insn-00bb9c00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9c94`](#insn-00bb9c94) → `002a568a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9ca0`](#insn-00bb9ca0) → [`00be1470`](../00be1/00be1470.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1470` · 推定シンボル `None` · 推定型 `None`
- [`00bb9ca4`](#insn-00bb9ca4) → `010a2890`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb9cac`](#insn-00bb9cac) → `010a2898`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb9cb0`](#insn-00bb9cb0) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00bb9cb4`](#insn-00bb9cb4) → [`00bb9c00`](#insn-00bb9c00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb9bb4`](#insn-00bb9bb4)

~~~json
{
  "source": "00bb9bb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9bb8`](#insn-00bb9bb8)

~~~json
{
  "source": "00bb9bb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9bbc`](#insn-00bb9bbc)

~~~json
{
  "source": "00bb9bbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9bc0`](#insn-00bb9bc0)

~~~json
{
  "source": "00bb9bc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9bd0`](#insn-00bb9bd0)

~~~json
{
  "source": "00bb9bd0",
  "target": "00bb9c30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9bdc`](#insn-00bb9bdc)

~~~json
{
  "source": "00bb9bdc",
  "target": "00bdb170",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9bf8`](#insn-00bb9bf8)

~~~json
{
  "source": "00bb9bf8",
  "target": "010a2898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2898",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb9bfc`](#insn-00bb9bfc)

~~~json
{
  "source": "00bb9bfc",
  "target": "00bb9c80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c00`](#insn-00bb9c00)

~~~json
{
  "source": "00bb9c00",
  "target": "010a2890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2890",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb9c0c`](#insn-00bb9c0c)

~~~json
{
  "source": "00bb9c0c",
  "target": "00be1ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9c14`](#insn-00bb9c14)

~~~json
{
  "source": "00bb9c14",
  "target": "00bb9c44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c18`](#insn-00bb9c18)

~~~json
{
  "source": "00bb9c18",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c20`](#insn-00bb9c20)

~~~json
{
  "source": "00bb9c20",
  "target": "00bb9c54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c28`](#insn-00bb9c28)

~~~json
{
  "source": "00bb9c28",
  "target": "00bb9c5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c2c`](#insn-00bb9c2c)

~~~json
{
  "source": "00bb9c2c",
  "target": "00bb9c64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c38`](#insn-00bb9c38)

~~~json
{
  "source": "00bb9c38",
  "target": "002b1870",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c40`](#insn-00bb9c40)

~~~json
{
  "source": "00bb9c40",
  "target": "00bb9c64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c44`](#insn-00bb9c44)

~~~json
{
  "source": "00bb9c44",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c50`](#insn-00bb9c50)

~~~json
{
  "source": "00bb9c50",
  "target": "00bb9c64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c58`](#insn-00bb9c58)

~~~json
{
  "source": "00bb9c58",
  "target": "002b1870",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c64`](#insn-00bb9c64)

~~~json
{
  "source": "00bb9c64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c68`](#insn-00bb9c68)

~~~json
{
  "source": "00bb9c68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c6c`](#insn-00bb9c6c)

~~~json
{
  "source": "00bb9c6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c70`](#insn-00bb9c70)

~~~json
{
  "source": "00bb9c70",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c84`](#insn-00bb9c84)

~~~json
{
  "source": "00bb9c84",
  "target": "010a2898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2898",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb9c88`](#insn-00bb9c88)

~~~json
{
  "source": "00bb9c88",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9c8c`](#insn-00bb9c8c)

~~~json
{
  "source": "00bb9c8c",
  "target": "00bb9c00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9c94`](#insn-00bb9c94)

~~~json
{
  "source": "00bb9c94",
  "target": "002a568a",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9ca0`](#insn-00bb9ca0)

~~~json
{
  "source": "00bb9ca0",
  "target": "00be1470",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9ca4`](#insn-00bb9ca4)

~~~json
{
  "source": "00bb9ca4",
  "target": "010a2890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2890",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb9cac`](#insn-00bb9cac)

~~~json
{
  "source": "00bb9cac",
  "target": "010a2898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2898",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb9cb0`](#insn-00bb9cb0)

~~~json
{
  "source": "00bb9cb0",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9cb4`](#insn-00bb9cb4)

~~~json
{
  "source": "00bb9cb4",
  "target": "00bb9c00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
