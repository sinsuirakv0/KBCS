# 00bfa5ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf95f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf95f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-d0270ba30ffbca25f4b03346466ce99c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa5ec",
  "name": "_ZNSt6__ndk115future_categoryEv",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3105720acfa0299f93ed656caf1a2657151cad9ce776f202db59ce8f3b9185a6",
  "source_text_sha256": "3105720acfa0299f93ed656caf1a2657151cad9ce776f202db59ce8f3b9185a6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfa5ec",
        "00bfa63b"
      ]
    ],
    "bytes_sha256": "cf41345dcc82700c7c9345aa174ecdbe4feb27e8afb9243751941cc5b0748126",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c593b0](../00c59/00c593b0.md)

## 呼び出し先

- [00c58ef0](../00c58/00c58ef0.md)
- [00c58f10](../00c58/00c58f10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 236 bytes

~~~c

undefined * _ZNSt6__ndk115future_categoryEv(void)

{
  int iVar1;
  
  if (((DAT_01128430 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01128430), iVar1 != 0)) {
    __cxa_guard_release(&DAT_01128430);
  }
  return &DAT_00ca5898;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfa5ec"></a> `00bfa5ec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfa5f0"></a> `00bfa5f0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfa5f4"></a> `00bfa5f4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfa5f8"></a> `00bfa5f8` | `68 29 00 d0` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00bfa5fc"></a> `00bfa5fc` | `08 c1 10 91` | add x8,x8,#0x430 | `FALL_THROUGH`
<a id="insn-00bfa600"></a> `00bfa600` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bfa604"></a> `00bfa604` | `c8 00 00 36` | tbz w8,#0x0,0x00bfa61c | `CONDITIONAL_JUMP`
<a id="insn-00bfa608"></a> `00bfa608` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bfa60c"></a> `00bfa60c` | `60 94 55 10` | adr x0,0xca5898 | `FALL_THROUGH`
<a id="insn-00bfa610"></a> `00bfa610` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bfa614"></a> `00bfa614` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfa618"></a> `00bfa618` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfa61c"></a> `00bfa61c` | `60 29 00 d0` | adrp x0,0x1128000 | `FALL_THROUGH`
<a id="insn-00bfa620"></a> `00bfa620` | `00 c0 10 91` | add x0,x0,#0x430 | `FALL_THROUGH`
<a id="insn-00bfa624"></a> `00bfa624` | `33 7a 01 94` | bl 0x00c58ef0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa628"></a> `00bfa628` | `00 ff ff 34` | cbz w0,0x00bfa608 | `CONDITIONAL_JUMP`
<a id="insn-00bfa62c"></a> `00bfa62c` | `60 29 00 d0` | adrp x0,0x1128000 | `FALL_THROUGH`
<a id="insn-00bfa630"></a> `00bfa630` | `00 c0 10 91` | add x0,x0,#0x430 | `FALL_THROUGH`
<a id="insn-00bfa634"></a> `00bfa634` | `37 7a 01 94` | bl 0x00c58f10 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa638"></a> `00bfa638` | `f4 ff ff 17` | b 0x00bfa608 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfa5ec`](#insn-00bfa5ec) 範囲 `[['00bfa5ec', '00bfa607']]`
  - `CONDITIONAL_JUMP` [`00bfa604`](#insn-00bfa604) → [`00bfa61c`](#insn-00bfa61c)
  - `FALL_THROUGH` [`00bfa604`](#insn-00bfa604) → [`00bfa608`](#insn-00bfa608)
- ブロック [`00bfa608`](#insn-00bfa608) 範囲 `[['00bfa608', '00bfa61b']]`
- ブロック [`00bfa61c`](#insn-00bfa61c) 範囲 `[['00bfa61c', '00bfa62b']]`
  - `CONDITIONAL_JUMP` [`00bfa628`](#insn-00bfa628) → [`00bfa608`](#insn-00bfa608)
  - `FALL_THROUGH` [`00bfa628`](#insn-00bfa628) → [`00bfa62c`](#insn-00bfa62c)
- ブロック [`00bfa62c`](#insn-00bfa62c) 範囲 `[['00bfa62c', '00bfa63b']]`
  - `UNCONDITIONAL_JUMP` [`00bfa638`](#insn-00bfa638) → [`00bfa608`](#insn-00bfa608)

## 命令位置別の参照

- [`00bfa5f0`](#insn-00bfa5f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa600`](#insn-00bfa600) → `01128430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfa604`](#insn-00bfa604) → [`00bfa61c`](#insn-00bfa61c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa60c`](#insn-00bfa60c) → `00ca5898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa610`](#insn-00bfa610) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa620`](#insn-00bfa620) → `01128430`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfa624`](#insn-00bfa624) → [`00c58ef0`](../00c58/00c58ef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ef0` · 推定シンボル `None` · 推定型 `None`
- [`00bfa628`](#insn-00bfa628) → [`00bfa608`](#insn-00bfa608) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa630`](#insn-00bfa630) → `01128430`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfa634`](#insn-00bfa634) → [`00c58f10`](../00c58/00c58f10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f10` · 推定シンボル `None` · 推定型 `None`
- [`00bfa638`](#insn-00bfa638) → [`00bfa608`](#insn-00bfa608) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfa5f0`](#insn-00bfa5f0)

~~~json
{
  "source": "00bfa5f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa600`](#insn-00bfa600)

~~~json
{
  "source": "00bfa600",
  "target": "01128430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128430",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfa604`](#insn-00bfa604)

~~~json
{
  "source": "00bfa604",
  "target": "00bfa61c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa60c`](#insn-00bfa60c)

~~~json
{
  "source": "00bfa60c",
  "target": "00ca5898",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa610`](#insn-00bfa610)

~~~json
{
  "source": "00bfa610",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa620`](#insn-00bfa620)

~~~json
{
  "source": "00bfa620",
  "target": "01128430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128430",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfa624`](#insn-00bfa624)

~~~json
{
  "source": "00bfa624",
  "target": "00c58ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa628`](#insn-00bfa628)

~~~json
{
  "source": "00bfa628",
  "target": "00bfa608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa630`](#insn-00bfa630)

~~~json
{
  "source": "00bfa630",
  "target": "01128430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128430",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfa634`](#insn-00bfa634)

~~~json
{
  "source": "00bfa634",
  "target": "00c58f10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa638`](#insn-00bfa638)

~~~json
{
  "source": "00bfa638",
  "target": "00bfa608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
