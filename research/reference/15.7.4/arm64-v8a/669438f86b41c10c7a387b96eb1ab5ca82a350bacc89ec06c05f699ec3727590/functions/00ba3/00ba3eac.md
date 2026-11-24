# 00ba3eac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ba3e68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3e68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0076.md#compare-ce54127ff3a94fdc93e7f486035604a1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c208f4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c208f4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-9df7f5d0e6db6a285fadbf50eccecc66)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba3eac",
  "name": "FUN_00ba3eac",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4464f4e206e1fd7bec586fd192a0e913dfeed4272346a817c13771c36c45b79c",
  "source_text_sha256": "4464f4e206e1fd7bec586fd192a0e913dfeed4272346a817c13771c36c45b79c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba3eac",
        "00ba3f1f"
      ]
    ],
    "bytes_sha256": "a362fb7f05df11328b3ea25329174048ba365603b7efc73c59476cfda2ed26ff",
    "instruction_count": 29,
    "instruction_bytes": 116,
    "body_bytes": 116,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ba261c](../00ba2/00ba261c.md)
- [00ba4ab8](../00ba4/00ba4ab8.md)

## 呼び出し先

- [00be18f0](../00be1/00be18f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 599 bytes

~~~c

void FUN_00ba3eac(long *param_1,byte *param_2,long param_3)

{
  byte *pbVar1;
  
  *param_1 = (long)(PTR__ZTVNSt6__ndk117moneypunct_bynameIcLb1EEE_00c1bf70 + 0x10);
  param_1[1] = param_3 + -1;
  param_1[4] = 0;
  param_1[3] = 0;
  param_1[6] = 0;
  param_1[5] = 0;
  param_1[8] = 0;
  param_1[7] = 0;
  param_1[10] = 0;
  param_1[9] = 0;
  param_1[0xc] = 0;
  param_1[0xb] = 0;
  param_1[0xe] = 0;
  param_1[0xd] = 0;
  pbVar1 = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    pbVar1 = param_2 + 1;
  }
  _ZNSt6__ndk117moneypunct_bynameIcLb1EE4initEPKc(param_1,pbVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba3eac"></a> `00ba3eac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00ba3eb0"></a> `00ba3eb0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ba3eb4"></a> `00ba3eb4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba3eb8"></a> `00ba3eb8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba3ebc"></a> `00ba3ebc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ba3ec0"></a> `00ba3ec0` | `c8 03 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00ba3ec4"></a> `00ba3ec4` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00ba3ec8"></a> `00ba3ec8` | `49 04 00 d1` | sub x9,x2,#0x1 | `FALL_THROUGH`
<a id="insn-00ba3ecc"></a> `00ba3ecc` | `08 b9 47 f9` | ldr x8,[x8, #0xf70] | `FALL_THROUGH`
<a id="insn-00ba3ed0"></a> `00ba3ed0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ba3ed4"></a> `00ba3ed4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ba3ed8"></a> `00ba3ed8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00ba3edc"></a> `00ba3edc` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00ba3ee0"></a> `00ba3ee0` | `a0 8e 81 3c` | str q0,[x21, #0x18]! | `FALL_THROUGH`
<a id="insn-00ba3ee4"></a> `00ba3ee4` | `00 80 82 3c` | stur q0,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00ba3ee8"></a> `00ba3ee8` | `00 80 83 3c` | stur q0,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00ba3eec"></a> `00ba3eec` | `00 80 84 3c` | stur q0,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00ba3ef0"></a> `00ba3ef0` | `00 80 85 3c` | stur q0,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00ba3ef4"></a> `00ba3ef4` | `00 80 86 3c` | stur q0,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00ba3ef8"></a> `00ba3ef8` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00ba3efc"></a> `00ba3efc` | `29 08 40 f9` | ldr x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00ba3f00"></a> `00ba3f00` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba3f04"></a> `00ba3f04` | `21 15 81 9a` | csinc x1,x9,x1,ne | `FALL_THROUGH`
<a id="insn-00ba3f08"></a> `00ba3f08` | `7a f6 00 94` | bl 0x00be18f0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba3f0c"></a> `00ba3f0c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba3f10"></a> `00ba3f10` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba3f14"></a> `00ba3f14` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ba3f18"></a> `00ba3f18` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00ba3f1c"></a> `00ba3f1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba3eac`](#insn-00ba3eac) 範囲 `[['00ba3eac', '00ba3f1f']]`

## 命令位置別の参照

- [`00ba3eb0`](#insn-00ba3eb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba3eb4`](#insn-00ba3eb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba3eb8`](#insn-00ba3eb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba3ecc`](#insn-00ba3ecc) → `00c1bf70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ba3edc`](#insn-00ba3edc) → `00c156e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[112]`
- [`00ba3f08`](#insn-00ba3f08) → [`00be18f0`](../00be1/00be18f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be18f0` · 推定シンボル `None` · 推定型 `None`
- [`00ba3f0c`](#insn-00ba3f0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba3f10`](#insn-00ba3f10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba3f14`](#insn-00ba3f14) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba3eb0`](#insn-00ba3eb0)

~~~json
{
  "source": "00ba3eb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba3eb4`](#insn-00ba3eb4)

~~~json
{
  "source": "00ba3eb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba3eb8`](#insn-00ba3eb8)

~~~json
{
  "source": "00ba3eb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba3ecc`](#insn-00ba3ecc)

~~~json
{
  "source": "00ba3ecc",
  "target": "00c1bf70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bf70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ba3edc`](#insn-00ba3edc)

~~~json
{
  "source": "00ba3edc",
  "target": "00c156e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c156d0",
  "offset": 16,
  "size": 112,
  "datatype": "undefined1[112]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00ba3f08`](#insn-00ba3f08)

~~~json
{
  "source": "00ba3f08",
  "target": "00be18f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba3f0c`](#insn-00ba3f0c)

~~~json
{
  "source": "00ba3f0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba3f10`](#insn-00ba3f10)

~~~json
{
  "source": "00ba3f10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba3f14`](#insn-00ba3f14)

~~~json
{
  "source": "00ba3f14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
