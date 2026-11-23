# 00bdbda0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbcf0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbcf0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-f22cf87cb8d3451b97785c449ceaa2cc)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbdf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdf0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-0515eb5ec5c10021d393c775a2e4eff4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbda0",
  "name": "_ZN5Botan6BigIntmIERKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f1e2dd070b8d6d365fbaf0beddf9c58ff0838ec194e26c05de1ea63e2440972a",
  "source_text_sha256": "f1e2dd070b8d6d365fbaf0beddf9c58ff0838ec194e26c05de1ea63e2440972a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbda0",
        "00bdbdaf"
      ]
    ],
    "bytes_sha256": "8f678e4df4ec0b54b70e121ec22754fcb147b3bf93256f24155e1b05dc30271d",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00493850](../00493/00493850.md)
- [004989ec](../00498/004989ec.md)
- [004b77d0](../004b7/004b77d0.md)
- [004b8aa0](../004b8/004b8aa0.md)
- [004b8bd8](../004b8/004b8bd8.md)
- [004b8e58](../004b8/004b8e58.md)
- [004ba430](../004ba/004ba430.md)
- [004bcf24](../004bc/004bcf24.md)
- [004be0f4](../004be/004be0f4.md)

## 呼び出し先

- [00495e3c](../00495/00495e3c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

void _ZN5Botan6BigIntmIERKS0_(void)

{
  (*(code *)PTR__ZN5Botan6BigIntmIERKS0__00c1c760)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbda0"></a> `00bdbda0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbda4"></a> `00bdbda4` | `11 b2 43 f9` | ldr x17,[x16, #0x760] | `FALL_THROUGH`
<a id="insn-00bdbda8"></a> `00bdbda8` | `10 82 1d 91` | add x16,x16,#0x760 | `FALL_THROUGH`
<a id="insn-00bdbdac"></a> `00bdbdac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbda0`](#insn-00bdbda0) 範囲 `[['00bdbda0', '00bdbdaf']]`

## 命令位置別の参照

- [`00bdbda4`](#insn-00bdbda4) → `00c1c760`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbdac`](#insn-00bdbdac) → [`00495e3c`](../00495/00495e3c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00495e3c` · 推定シンボル `_ZN5Botan6BigIntmIERKS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbda4`](#insn-00bdbda4)

~~~json
{
  "source": "00bdbda4",
  "target": "00c1c760",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c760",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbdac`](#insn-00bdbdac)

~~~json
{
  "source": "00bdbdac",
  "target": "00495e3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
