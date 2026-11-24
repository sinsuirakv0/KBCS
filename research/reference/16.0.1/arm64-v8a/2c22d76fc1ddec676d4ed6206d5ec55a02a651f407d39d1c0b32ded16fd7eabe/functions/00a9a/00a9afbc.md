# 00a9afbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0082.md#review-4b287365d9b01ea200ffa4766a70938b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0041.md#review-4b287365d9b01ea200ffa4766a70938b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9afbc",
  "name": "FUN_00a9afbc",
  "size": 196,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42b77fe8218090744dbe07ebe561fb9c83af9d2fe03b330366580f8579ec45a7",
  "source_text_sha256": "42b77fe8218090744dbe07ebe561fb9c83af9d2fe03b330366580f8579ec45a7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9afbc",
        "00a9b07f"
      ]
    ],
    "bytes_sha256": "7f5dc43ecab47a2fda7f2afe9d81707bb795090a27746efce5b19ef6b2b57fbf",
    "instruction_count": 49,
    "instruction_bytes": 196,
    "body_bytes": 196,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0048ccf8](../0048c/0048ccf8.md)
- [0048e7e0](../0048e/0048e7e0.md)
- [0066d0dc](../0066d/0066d0dc.md)
- [00a605b4](../00a60/00a605b4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 925 bytes

~~~c

void FUN_00a9afbc(long param_1,byte *param_2)

{
  ulong uVar1;
  long lVar2;
  
  lVar2 = *(long *)(param_1 + 8);
  if ((*param_2 & 1) == 0) {
    *(undefined1 *)(*(long *)(lVar2 + 0x2268) + 0x20) = 0;
  }
  *(undefined1 *)((long)&DWORD_0039b1d8 + lVar2) = 0;
  FUN_0048ccf8();
  FUN_0048e7e0();
  FUN_0066d0dc(0xe);
  *(undefined4 *)((long)&fde_table_entry_00333970.data_loc + lVar2) = 3;
  *(undefined4 *)((long)&fde_0038f284 + lVar2) = 3;
  *(undefined1 *)(lVar2 + 0x33d9) = 1;
  *(undefined4 *)((long)&fde_table_entry_00332068.initial_loc + lVar2) = 0;
  uVar1 = FUN_00a605b4(lVar2 + 0x23a0);
  if ((uVar1 & 1) != 0) {
    *(undefined4 *)((long)&fde_table_entry_00332068.initial_loc + lVar2) = 1;
    *(undefined1 *)((long)&fde_table_entry_003372c8.data_loc + lVar2) = 1;
  }
  *(undefined1 *)((long)&fde_table_entry_00332060.initial_loc + lVar2) = 1;
  *(undefined4 *)((long)&DWORD_003c7c6c + lVar2) = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a9afbc"></a> `00a9afbc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00a9afc0"></a> `00a9afc0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9afc4"></a> `00a9afc4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9afc8"></a> `00a9afc8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a9afcc"></a> `00a9afcc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a9afd0"></a> `00a9afd0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a9afd4"></a> `00a9afd4` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a9afd8"></a> `00a9afd8` | `93 8d 8f 52` | mov w19,#0x7c6c | `FALL_THROUGH`
<a id="insn-00a9afdc"></a> `00a9afdc` | `29 00 40 39` | ldrb w9,[x1] | `FALL_THROUGH`
<a id="insn-00a9afe0"></a> `00a9afe0` | `08 3b 96 52` | mov w8,#0xb1d8 | `FALL_THROUGH`
<a id="insn-00a9afe4"></a> `00a9afe4` | `96 50 9e 52` | mov w22,#0xf284 | `FALL_THROUGH`
<a id="insn-00a9afe8"></a> `00a9afe8` | `97 2e 87 52` | mov w23,#0x3974 | `FALL_THROUGH`
<a id="insn-00a9afec"></a> `00a9afec` | `8a ca 4c 91` | add x10,x20,#0x332, LSL #12 | `FALL_THROUGH`
<a id="insn-00a9aff0"></a> `00a9aff0` | `93 07 a0 72` | movk w19,#0x3c, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9aff4"></a> `00a9aff4` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9aff8"></a> `00a9aff8` | `16 07 a0 72` | movk w22,#0x38, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9affc"></a> `00a9affc` | `77 06 a0 72` | movk w23,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9b000"></a> `00a9b000` | `55 81 01 91` | add x21,x10,#0x60 | `FALL_THROUGH`
<a id="insn-00a9b004"></a> `00a9b004` | `38 7b 86 52` | mov w24,#0x33d9 | `FALL_THROUGH`
<a id="insn-00a9b008"></a> `00a9b008` | `69 00 00 37` | tbnz w9,#0x0,0x00a9b014 | `CONDITIONAL_JUMP`
<a id="insn-00a9b00c"></a> `00a9b00c` | `89 36 51 f9` | ldr x9,[x20, #0x2268] | `FALL_THROUGH`
<a id="insn-00a9b010"></a> `00a9b010` | `3f 81 00 39` | strb wzr,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00a9b014"></a> `00a9b014` | `9f 6a 28 38` | strb wzr,[x20, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a9b018"></a> `00a9b018` | `38 c7 e7 97` | bl 0x0048ccf8 | `UNCONDITIONAL_CALL`
<a id="insn-00a9b01c"></a> `00a9b01c` | `f1 cd e7 97` | bl 0x0048e7e0 | `UNCONDITIONAL_CALL`
<a id="insn-00a9b020"></a> `00a9b020` | `c0 01 80 52` | mov w0,#0xe | `FALL_THROUGH`
<a id="insn-00a9b024"></a> `00a9b024` | `2e 48 ef 97` | bl 0x0066d0dc | `UNCONDITIONAL_CALL`
<a id="insn-00a9b028"></a> `00a9b028` | `68 00 80 52` | mov w8,#0x3 | `FALL_THROUGH`
<a id="insn-00a9b02c"></a> `00a9b02c` | `88 6a 37 b8` | str w8,[x20, x23, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9b030"></a> `00a9b030` | `39 00 80 52` | mov w25,#0x1 | `FALL_THROUGH`
<a id="insn-00a9b034"></a> `00a9b034` | `88 6a 36 b8` | str w8,[x20, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9b038"></a> `00a9b038` | `08 74 84 52` | mov w8,#0x23a0 | `FALL_THROUGH`
<a id="insn-00a9b03c"></a> `00a9b03c` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00a9b040"></a> `00a9b040` | `99 6a 38 38` | strb w25,[x20, x24, LSL ] | `FALL_THROUGH`
<a id="insn-00a9b044"></a> `00a9b044` | `bf 0a 00 b9` | str wzr,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00a9b048"></a> `00a9b048` | `5b 15 ff 97` | bl 0x00a605b4 | `UNCONDITIONAL_CALL`
<a id="insn-00a9b04c"></a> `00a9b04c` | `a0 00 00 36` | tbz w0,#0x0,0x00a9b060 | `CONDITIONAL_JUMP`
<a id="insn-00a9b050"></a> `00a9b050` | `88 59 8e 52` | mov w8,#0x72cc | `FALL_THROUGH`
<a id="insn-00a9b054"></a> `00a9b054` | `b9 0a 00 b9` | str w25,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00a9b058"></a> `00a9b058` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9b05c"></a> `00a9b05c` | `99 6a 28 38` | strb w25,[x20, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a9b060"></a> `00a9b060` | `b9 02 00 39` | strb w25,[x21] | `FALL_THROUGH`
<a id="insn-00a9b064"></a> `00a9b064` | `9f 6a 33 b8` | str wzr,[x20, x19, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9b068"></a> `00a9b068` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a9b06c"></a> `00a9b06c` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9b070"></a> `00a9b070` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a9b074"></a> `00a9b074` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9b078"></a> `00a9b078` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00a9b07c"></a> `00a9b07c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9afbc`](#insn-00a9afbc) 範囲 `[['00a9afbc', '00a9b00b']]`
  - `CONDITIONAL_JUMP` [`00a9b008`](#insn-00a9b008) → [`00a9b014`](#insn-00a9b014)
  - `FALL_THROUGH` [`00a9b008`](#insn-00a9b008) → [`00a9b00c`](#insn-00a9b00c)
- ブロック [`00a9b00c`](#insn-00a9b00c) 範囲 `[['00a9b00c', '00a9b013']]`
  - `FALL_THROUGH` [`00a9b010`](#insn-00a9b010) → [`00a9b014`](#insn-00a9b014)
- ブロック [`00a9b014`](#insn-00a9b014) 範囲 `[['00a9b014', '00a9b04f']]`
  - `CONDITIONAL_JUMP` [`00a9b04c`](#insn-00a9b04c) → [`00a9b060`](#insn-00a9b060)
  - `FALL_THROUGH` [`00a9b04c`](#insn-00a9b04c) → [`00a9b050`](#insn-00a9b050)
- ブロック [`00a9b050`](#insn-00a9b050) 範囲 `[['00a9b050', '00a9b05f']]`
  - `FALL_THROUGH` [`00a9b05c`](#insn-00a9b05c) → [`00a9b060`](#insn-00a9b060)
- ブロック [`00a9b060`](#insn-00a9b060) 範囲 `[['00a9b060', '00a9b07f']]`

## 命令位置別の参照

- [`00a9afbc`](#insn-00a9afbc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9afc0`](#insn-00a9afc0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9afc4`](#insn-00a9afc4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9afc8`](#insn-00a9afc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9afcc`](#insn-00a9afcc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9b008`](#insn-00a9b008) → [`00a9b014`](#insn-00a9b014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9b014`](#insn-00a9b014) → `0039b1d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00a9b018`](#insn-00a9b018) → [`0048ccf8`](../0048c/0048ccf8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ccf8` · 推定シンボル `None` · 推定型 `None`
- [`00a9b01c`](#insn-00a9b01c) → [`0048e7e0`](../0048e/0048e7e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048e7e0` · 推定シンボル `None` · 推定型 `None`
- [`00a9b024`](#insn-00a9b024) → [`0066d0dc`](../0066d/0066d0dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0066d0dc` · 推定シンボル `None` · 推定型 `None`
- [`00a9b02c`](#insn-00a9b02c) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a9b034`](#insn-00a9b034) → `0038f284`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0038f284` · 推定型 `dword`
- [`00a9b044`](#insn-00a9b044) → `00332068`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a9b048`](#insn-00a9b048) → [`00a605b4`](../00a60/00a605b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a605b4` · 推定シンボル `None` · 推定型 `None`
- [`00a9b04c`](#insn-00a9b04c) → [`00a9b060`](#insn-00a9b060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9b054`](#insn-00a9b054) → `00332068`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a9b05c`](#insn-00a9b05c) → `003372cc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a9b060`](#insn-00a9b060) → `00332060`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a9b064`](#insn-00a9b064) → `003c7c6c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00a9b068`](#insn-00a9b068) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9b06c`](#insn-00a9b06c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9b070`](#insn-00a9b070) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9b074`](#insn-00a9b074) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9b078`](#insn-00a9b078) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9afbc`](#insn-00a9afbc)

~~~json
{
  "source": "00a9afbc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9afc0`](#insn-00a9afc0)

~~~json
{
  "source": "00a9afc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9afc4`](#insn-00a9afc4)

~~~json
{
  "source": "00a9afc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9afc8`](#insn-00a9afc8)

~~~json
{
  "source": "00a9afc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9afcc`](#insn-00a9afcc)

~~~json
{
  "source": "00a9afcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9b008`](#insn-00a9b008)

~~~json
{
  "source": "00a9b008",
  "target": "00a9b014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9b014`](#insn-00a9b014)

~~~json
{
  "source": "00a9b014",
  "target": "0039b1d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b1d8",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "287b0500",
  "capture_start": "0039b1d8",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9b018`](#insn-00a9b018)

~~~json
{
  "source": "00a9b018",
  "target": "0048ccf8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9b01c`](#insn-00a9b01c)

~~~json
{
  "source": "00a9b01c",
  "target": "0048e7e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9b024`](#insn-00a9b024)

~~~json
{
  "source": "00a9b024",
  "target": "0066d0dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9b02c`](#insn-00a9b02c)

~~~json
{
  "source": "00a9b02c",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9b034`](#insn-00a9b034)

~~~json
{
  "source": "00a9b034",
  "target": "0038f284",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038f284",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0038f284",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9b044`](#insn-00a9b044)

~~~json
{
  "source": "00a9b044",
  "target": "00332068",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332068",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e004620078240900",
  "capture_start": "00332068",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9b048`](#insn-00a9b048)

~~~json
{
  "source": "00a9b048",
  "target": "00a605b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9b04c`](#insn-00a9b04c)

~~~json
{
  "source": "00a9b04c",
  "target": "00a9b060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9b054`](#insn-00a9b054)

~~~json
{
  "source": "00a9b054",
  "target": "00332068",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332068",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e004620078240900",
  "capture_start": "00332068",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9b05c`](#insn-00a9b05c)

~~~json
{
  "source": "00a9b05c",
  "target": "003372cc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003372c8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "a83f7a00383d0a00",
  "capture_start": "003372c8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9b060`](#insn-00a9b060)

~~~json
{
  "source": "00a9b060",
  "target": "00332060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332060",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "cc04620064240900",
  "capture_start": "00332060",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9b064`](#insn-00a9b064)

~~~json
{
  "source": "00a9b064",
  "target": "003c7c6c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003c7c6c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "e8e97700",
  "capture_start": "003c7c6c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9b068`](#insn-00a9b068)

~~~json
{
  "source": "00a9b068",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9b06c`](#insn-00a9b06c)

~~~json
{
  "source": "00a9b06c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9b070`](#insn-00a9b070)

~~~json
{
  "source": "00a9b070",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9b074`](#insn-00a9b074)

~~~json
{
  "source": "00a9b074",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9b078`](#insn-00a9b078)

~~~json
{
  "source": "00a9b078",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
