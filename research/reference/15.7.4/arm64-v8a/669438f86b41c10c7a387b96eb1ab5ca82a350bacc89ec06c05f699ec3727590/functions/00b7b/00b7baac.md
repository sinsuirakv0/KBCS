# 00b7baac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7ba68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7ba68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-dc5e308aedea4a3b4dddec8f1e83bf58)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf84f4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf84f4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0071.md#compare-74968de06610268fc17e513edd280d83)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7baac",
  "name": "_ZNSt6__ndk112system_errorC1ENS_10error_codeERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e04ad5a3849f2b2f3f91288d2371f49edc295f716c9b1f615ba1041fc53cac81",
  "source_text_sha256": "e04ad5a3849f2b2f3f91288d2371f49edc295f716c9b1f615ba1041fc53cac81",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7baac",
        "00b7bb57"
      ]
    ],
    "bytes_sha256": "02604b7eb5eadf8b5a65a10d8aa9dca87bec58806c9c2fa4338c32a51d799abf",
    "instruction_count": 43,
    "instruction_bytes": 172,
    "body_bytes": 172,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1150](../00be1/00be1150.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [00b7bba4](../00b7b/00b7bba4.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00be0fa0](../00be0/00be0fa0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 972 bytes

~~~c

void _ZNSt6__ndk112system_errorC1ENS_10error_codeERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
               (long *param_1,long param_2,long param_3,ulong *param_4)

{
  ulong local_60;
  ulong uStack_58;
  void *local_50;
  byte local_48 [16];
  void *local_38;
  long local_30;
  long lStack_28;
  
  local_30 = param_2;
  lStack_28 = param_3;
  if ((*param_4 & 1) == 0) {
    uStack_58 = param_4[1];
    local_60 = *param_4;
    local_50 = (void *)param_4[2];
  }
  else {
    FUN_00418fe0(&local_60,param_4[2],param_4[1]);
  }
  FUN_00b7bba4(local_48,&local_30,&local_60);
  _ZNSt13runtime_errorC2ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
            (param_1,local_48);
  if ((local_48[0] & 1) != 0) {
    _ZdlPv(local_38);
  }
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  *param_1 = (long)(PTR__ZTVNSt6__ndk112system_errorE_00c1bca0 + 0x10);
  param_1[3] = lStack_28;
  param_1[2] = local_30;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7baac"></a> `00b7baac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b7bab0"></a> `00b7bab0` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b7bab4"></a> `00b7bab4` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b7bab8"></a> `00b7bab8` | `f3 2b 00 f9` | str x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b7babc"></a> `00b7babc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b7bac0"></a> `00b7bac0` | `68 00 40 39` | ldrb w8,[x3] | `FALL_THROUGH`
<a id="insn-00b7bac4"></a> `00b7bac4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b7bac8"></a> `00b7bac8` | `a1 0b 3f a9` | stp x1,x2,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00b7bacc"></a> `00b7bacc` | `c8 00 00 37` | tbnz w8,#0x0,0x00b7bae4 | `CONDITIONAL_JUMP`
<a id="insn-00b7bad0"></a> `00b7bad0` | `60 00 c0 3d` | ldr q0,[x3] | `FALL_THROUGH`
<a id="insn-00b7bad4"></a> `00b7bad4` | `68 08 40 f9` | ldr x8,[x3, #0x10] | `FALL_THROUGH`
<a id="insn-00b7bad8"></a> `00b7bad8` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00b7badc"></a> `00b7badc` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7bae0"></a> `00b7bae0` | `04 00 00 14` | b 0x00b7baf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b7bae4"></a> `00b7bae4` | `62 84 40 a9` | ldp x2,x1,[x3, #0x8] | `FALL_THROUGH`
<a id="insn-00b7bae8"></a> `00b7bae8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00b7baec"></a> `00b7baec` | `3d 75 e2 97` | bl 0x00418fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7baf0"></a> `00b7baf0` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b7baf4"></a> `00b7baf4` | `a0 43 00 d1` | sub x0,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00b7baf8"></a> `00b7baf8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00b7bafc"></a> `00b7bafc` | `2a 00 00 94` | bl 0x00b7bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00b7bb00"></a> `00b7bb00` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b7bb04"></a> `00b7bb04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7bb08"></a> `00b7bb08` | `26 95 01 94` | bl 0x00be0fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7bb0c"></a> `00b7bb0c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b7bb10"></a> `00b7bb10` | `68 00 00 36` | tbz w8,#0x0,0x00b7bb1c | `CONDITIONAL_JUMP`
<a id="insn-00b7bb14"></a> `00b7bb14` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b7bb18"></a> `00b7bb18` | `52 7d 01 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b7bb1c"></a> `00b7bb1c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b7bb20"></a> `00b7bb20` | `68 00 00 36` | tbz w8,#0x0,0x00b7bb2c | `CONDITIONAL_JUMP`
<a id="insn-00b7bb24"></a> `00b7bb24` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7bb28"></a> `00b7bb28` | `4e 7d 01 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b7bb2c"></a> `00b7bb2c` | `08 05 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b7bb30"></a> `00b7bb30` | `08 51 46 f9` | ldr x8,[x8, #0xca0] | `FALL_THROUGH`
<a id="insn-00b7bb34"></a> `00b7bb34` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00b7bb38"></a> `00b7bb38` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b7bb3c"></a> `00b7bb3c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00b7bb40"></a> `00b7bb40` | `60 06 80 3d` | str q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b7bb44"></a> `00b7bb44` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b7bb48"></a> `00b7bb48` | `f3 2b 40 f9` | ldr x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b7bb4c"></a> `00b7bb4c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b7bb50"></a> `00b7bb50` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b7bb54"></a> `00b7bb54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7baac`](#insn-00b7baac) 範囲 `[['00b7baac', '00b7bacf']]`
  - `CONDITIONAL_JUMP` [`00b7bacc`](#insn-00b7bacc) → [`00b7bae4`](#insn-00b7bae4)
  - `FALL_THROUGH` [`00b7bacc`](#insn-00b7bacc) → [`00b7bad0`](#insn-00b7bad0)
- ブロック [`00b7bad0`](#insn-00b7bad0) 範囲 `[['00b7bad0', '00b7bae3']]`
  - `UNCONDITIONAL_JUMP` [`00b7bae0`](#insn-00b7bae0) → [`00b7baf0`](#insn-00b7baf0)
- ブロック [`00b7bae4`](#insn-00b7bae4) 範囲 `[['00b7bae4', '00b7baef']]`
  - `FALL_THROUGH` [`00b7baec`](#insn-00b7baec) → [`00b7baf0`](#insn-00b7baf0)
- ブロック [`00b7baf0`](#insn-00b7baf0) 範囲 `[['00b7baf0', '00b7bb13']]`
  - `CONDITIONAL_JUMP` [`00b7bb10`](#insn-00b7bb10) → [`00b7bb1c`](#insn-00b7bb1c)
  - `FALL_THROUGH` [`00b7bb10`](#insn-00b7bb10) → [`00b7bb14`](#insn-00b7bb14)
- ブロック [`00b7bb14`](#insn-00b7bb14) 範囲 `[['00b7bb14', '00b7bb1b']]`
  - `FALL_THROUGH` [`00b7bb18`](#insn-00b7bb18) → [`00b7bb1c`](#insn-00b7bb1c)
- ブロック [`00b7bb1c`](#insn-00b7bb1c) 範囲 `[['00b7bb1c', '00b7bb23']]`
  - `CONDITIONAL_JUMP` [`00b7bb20`](#insn-00b7bb20) → [`00b7bb2c`](#insn-00b7bb2c)
  - `FALL_THROUGH` [`00b7bb20`](#insn-00b7bb20) → [`00b7bb24`](#insn-00b7bb24)
- ブロック [`00b7bb24`](#insn-00b7bb24) 範囲 `[['00b7bb24', '00b7bb2b']]`
  - `FALL_THROUGH` [`00b7bb28`](#insn-00b7bb28) → [`00b7bb2c`](#insn-00b7bb2c)
- ブロック [`00b7bb2c`](#insn-00b7bb2c) 範囲 `[['00b7bb2c', '00b7bb57']]`

## 命令位置別の参照

- [`00b7bab4`](#insn-00b7bab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bab8`](#insn-00b7bab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bac8`](#insn-00b7bac8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bacc`](#insn-00b7bacc) → [`00b7bae4`](#insn-00b7bae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bad8`](#insn-00b7bad8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7badc`](#insn-00b7badc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bae0`](#insn-00b7bae0) → [`00b7baf0`](#insn-00b7baf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7baec`](#insn-00b7baec) → [`00418fe0`](../00418/00418fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418fe0` · 推定シンボル `None` · 推定型 `None`
- [`00b7bafc`](#insn-00b7bafc) → [`00b7bba4`](00b7bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b7bba4` · 推定シンボル `None` · 推定型 `None`
- [`00b7bb08`](#insn-00b7bb08) → [`00be0fa0`](../00be0/00be0fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0fa0` · 推定シンボル `None` · 推定型 `None`
- [`00b7bb0c`](#insn-00b7bb0c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bb10`](#insn-00b7bb10) → [`00b7bb1c`](#insn-00b7bb1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bb14`](#insn-00b7bb14) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bb18`](#insn-00b7bb18) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b7bb1c`](#insn-00b7bb1c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bb20`](#insn-00b7bb20) → [`00b7bb2c`](#insn-00b7bb2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bb24`](#insn-00b7bb24) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bb28`](#insn-00b7bb28) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b7bb30`](#insn-00b7bb30) → `00c1bca0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b7bb34`](#insn-00b7bb34) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bb3c`](#insn-00b7bb3c) → `00c12dc8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00b7bb44`](#insn-00b7bb44) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bb48`](#insn-00b7bb48) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7bab4`](#insn-00b7bab4)

~~~json
{
  "source": "00b7bab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bab8`](#insn-00b7bab8)

~~~json
{
  "source": "00b7bab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bac8`](#insn-00b7bac8)

~~~json
{
  "source": "00b7bac8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bacc`](#insn-00b7bacc)

~~~json
{
  "source": "00b7bacc",
  "target": "00b7bae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bad8`](#insn-00b7bad8)

~~~json
{
  "source": "00b7bad8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7badc`](#insn-00b7badc)

~~~json
{
  "source": "00b7badc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bae0`](#insn-00b7bae0)

~~~json
{
  "source": "00b7bae0",
  "target": "00b7baf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7baec`](#insn-00b7baec)

~~~json
{
  "source": "00b7baec",
  "target": "00418fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7bafc`](#insn-00b7bafc)

~~~json
{
  "source": "00b7bafc",
  "target": "00b7bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7bb08`](#insn-00b7bb08)

~~~json
{
  "source": "00b7bb08",
  "target": "00be0fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7bb0c`](#insn-00b7bb0c)

~~~json
{
  "source": "00b7bb0c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bb10`](#insn-00b7bb10)

~~~json
{
  "source": "00b7bb10",
  "target": "00b7bb1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bb14`](#insn-00b7bb14)

~~~json
{
  "source": "00b7bb14",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bb18`](#insn-00b7bb18)

~~~json
{
  "source": "00b7bb18",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7bb1c`](#insn-00b7bb1c)

~~~json
{
  "source": "00b7bb1c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bb20`](#insn-00b7bb20)

~~~json
{
  "source": "00b7bb20",
  "target": "00b7bb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bb24`](#insn-00b7bb24)

~~~json
{
  "source": "00b7bb24",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bb28`](#insn-00b7bb28)

~~~json
{
  "source": "00b7bb28",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7bb30`](#insn-00b7bb30)

~~~json
{
  "source": "00b7bb30",
  "target": "00c1bca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bca0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b7bb34`](#insn-00b7bb34)

~~~json
{
  "source": "00b7bb34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bb3c`](#insn-00b7bb3c)

~~~json
{
  "source": "00b7bb3c",
  "target": "00c12dc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c12db8",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00b7bb44`](#insn-00b7bb44)

~~~json
{
  "source": "00b7bb44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bb48`](#insn-00b7bb48)

~~~json
{
  "source": "00b7bb48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
