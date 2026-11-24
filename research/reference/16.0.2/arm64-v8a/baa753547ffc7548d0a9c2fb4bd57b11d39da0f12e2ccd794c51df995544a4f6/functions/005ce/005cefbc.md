# 005cefbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `005cef7c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cef7c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0024.md#compare-0e8ef845fc09d4e33246fb7f86a0180f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `005cf36c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf36c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0024.md#compare-bc0d3c4c6716d26e7b71c463860c1b17)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cefbc",
  "name": "FUN_005cefbc",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f56aa53d419c36d27df3396e09301b5a8cb414b4dc7603570eeda33e181888a1",
  "source_text_sha256": "f56aa53d419c36d27df3396e09301b5a8cb414b4dc7603570eeda33e181888a1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005cefbc",
        "005cf013"
      ]
    ],
    "bytes_sha256": "57500a606815da08ac41494e243cbf4c3209b51ef07f157a33d47f1aad9a0158",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005ce640](../005ce/005ce640.md)

## 呼び出し先

- [00c58350](../00c58/00c58350.md)
- [00c5a870](../00c5a/00c5a870.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 584 bytes

~~~c

void FUN_005cefbc(long param_1)

{
  undefined8 uVar1;
  
  _ZNSt6__ndk16localeC2Ev();
  uVar1 = _ZNKSt6__ndk16locale9use_facetERNS0_2idE(param_1,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ad00);
  *(undefined8 *)(param_1 + 8) = uVar1;
  uVar1 = _ZNKSt6__ndk16locale9use_facetERNS0_2idE(param_1,PTR__ZNSt6__ndk17collateIcE2idE_00c9b448)
  ;
  *(undefined8 *)(param_1 + 0x10) = uVar1;
  *(undefined8 *)(param_1 + 0x20) = 0;
  *(undefined8 *)(param_1 + 0x18) = 0;
  *(undefined8 *)(param_1 + 0x30) = 0;
  *(undefined8 *)(param_1 + 0x28) = 0;
  *(undefined8 *)(param_1 + 0x38) = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005cefbc"></a> `005cefbc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-005cefc0"></a> `005cefc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005cefc4"></a> `005cefc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005cefc8"></a> `005cefc8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005cefcc"></a> `005cefcc` | `29 2e 1a 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-005cefd0"></a> `005cefd0` | `61 36 00 90` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-005cefd4"></a> `005cefd4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cefd8"></a> `005cefd8` | `21 80 46 f9` | ldr x1,[x1, #0xd00] | `FALL_THROUGH`
<a id="insn-005cefdc"></a> `005cefdc` | `dd 24 1a 94` | bl 0x00c58350 | `UNCONDITIONAL_CALL`
<a id="insn-005cefe0"></a> `005cefe0` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-005cefe4"></a> `005cefe4` | `61 36 00 b0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-005cefe8"></a> `005cefe8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cefec"></a> `005cefec` | `21 24 42 f9` | ldr x1,[x1, #0x448] | `FALL_THROUGH`
<a id="insn-005ceff0"></a> `005ceff0` | `d8 24 1a 94` | bl 0x00c58350 | `UNCONDITIONAL_CALL`
<a id="insn-005ceff4"></a> `005ceff4` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-005ceff8"></a> `005ceff8` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-005ceffc"></a> `005ceffc` | `60 82 81 3c` | stur q0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-005cf000"></a> `005cf000` | `60 82 82 3c` | stur q0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-005cf004"></a> `005cf004` | `7f 1e 00 f9` | str xzr,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-005cf008"></a> `005cf008` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005cf00c"></a> `005cf00c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-005cf010"></a> `005cf010` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005cefbc`](#insn-005cefbc) 範囲 `[['005cefbc', '005cf013']]`

## 命令位置別の参照

- [`005cefbc`](#insn-005cefbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cefc0`](#insn-005cefc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cefcc`](#insn-005cefcc) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`005cefd8`](#insn-005cefd8) → `00c9ad00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005cefd8`](#insn-005cefd8) → `01127f18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`005cefdc`](#insn-005cefdc) → [`00c58350`](../00c58/00c58350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58350` · 推定シンボル `None` · 推定型 `None`
- [`005cefec`](#insn-005cefec) → `00c9b448`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005cefec`](#insn-005cefec) → `01127c58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17collateIcE2idE` · 推定型 `undefined8`
- [`005ceff0`](#insn-005ceff0) → [`00c58350`](../00c58/00c58350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58350` · 推定シンボル `None` · 推定型 `None`
- [`005cf008`](#insn-005cf008) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cf00c`](#insn-005cf00c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005cefbc`](#insn-005cefbc)

~~~json
{
  "source": "005cefbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cefc0`](#insn-005cefc0)

~~~json
{
  "source": "005cefc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cefcc`](#insn-005cefcc)

~~~json
{
  "source": "005cefcc",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cefd8`](#insn-005cefd8)

~~~json
{
  "source": "005cefd8",
  "target": "00c9ad00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ad00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cefd8`](#insn-005cefd8)

~~~json
{
  "source": "005cefd8",
  "target": "01127f18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127f18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cefdc`](#insn-005cefdc)

~~~json
{
  "source": "005cefdc",
  "target": "00c58350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cefec`](#insn-005cefec)

~~~json
{
  "source": "005cefec",
  "target": "00c9b448",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b448",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cefec`](#insn-005cefec)

~~~json
{
  "source": "005cefec",
  "target": "01127c58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005ceff0`](#insn-005ceff0)

~~~json
{
  "source": "005ceff0",
  "target": "00c58350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cf008`](#insn-005cf008)

~~~json
{
  "source": "005cf008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cf00c`](#insn-005cf00c)

~~~json
{
  "source": "005cf00c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
