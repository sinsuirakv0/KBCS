# 00bdafc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdaf10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0005.md#compare-675516032491514cbe8db625abb28280)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdb010`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0012.md#compare-098b07acc11c7ca49f9ff3ab0761a2e1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdafc0",
  "name": "_ZNSt6__ndk15mutexD1Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a379457addcbf996dbf6523f518e94470eee35acc53cfb7c0a09224b8221a239",
  "source_text_sha256": "a379457addcbf996dbf6523f518e94470eee35acc53cfb7c0a09224b8221a239",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdafc0",
        "00bdafcf"
      ]
    ],
    "bytes_sha256": "d00f28db86ab31db7fb30fa359f2f568430d178039997730c70fd9a009890f15",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00428128](../00428/00428128.md)
- [0043bf90](../0043b/0043bf90.md)
- [0043bfdc](../0043b/0043bfdc.md)
- [0044e018](../0044e/0044e018.md)
- [00451c20](../00451/00451c20.md)
- [00451e24](../00451/00451e24.md)
- [0045ca50](../0045c/0045ca50.md)
- [00475a44](../00475/00475a44.md)
- [00475c54](../00475/00475c54.md)
- [004a7cbc](../004a7/004a7cbc.md)
- [004a7ed0](../004a7/004a7ed0.md)
- [005121d0](../00512/005121d0.md)
- [00512208](../00512/00512208.md)
- [005159e0](../00515/005159e0.md)
- [00515a90](../00515/00515a90.md)
- [00515f5c](../00515/00515f5c.md)
- [0051600c](../00516/0051600c.md)
- [005488c4](../00548/005488c4.md)
- [0056459c](../00564/0056459c.md)
- [00596708](../00596/00596708.md)
- [0067c7f0](../0067c/0067c7f0.md)
- [0075237c](../00752/0075237c.md)
- [00808774](../00808/00808774.md)
- [00814cc4](../00814/00814cc4.md)
- [00816114](../00816/00816114.md)
- [00816bf4](../00816/00816bf4.md)
- [00816ec4](../00816/00816ec4.md)
- [008456e4](../00845/008456e4.md)
- [00b7d1d4](../00b7d/00b7d1d4.md)
- [00b7d444](../00b7d/00b7d444.md)
- [00b7d5f8](../00b7d/00b7d5f8.md)

## 呼び出し先

- [00b7d25c](../00b7d/00b7d25c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 103 bytes

~~~c

void _ZNSt6__ndk15mutexD1Ev(void)

{
  (*(code *)PTR__ZNSt6__ndk15mutexD1Ev_00c1c070)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdafc0"></a> `00bdafc0` | `10 02 00 d0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdafc4"></a> `00bdafc4` | `11 3a 40 f9` | ldr x17,[x16, #0x70] | `FALL_THROUGH`
<a id="insn-00bdafc8"></a> `00bdafc8` | `10 c2 01 91` | add x16,x16,#0x70 | `FALL_THROUGH`
<a id="insn-00bdafcc"></a> `00bdafcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdafc0`](#insn-00bdafc0) 範囲 `[['00bdafc0', '00bdafcf']]`

## 命令位置別の参照

- [`00bdafc4`](#insn-00bdafc4) → `00c1c070`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdafcc`](#insn-00bdafcc) → [`00b7d25c`](../00b7d/00b7d25c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b7d25c` · 推定シンボル `_ZNSt6__ndk15mutexD1Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdafc4`](#insn-00bdafc4)

~~~json
{
  "source": "00bdafc4",
  "target": "00c1c070",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c070",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdafcc`](#insn-00bdafcc)

~~~json
{
  "source": "00bdafcc",
  "target": "00b7d25c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
