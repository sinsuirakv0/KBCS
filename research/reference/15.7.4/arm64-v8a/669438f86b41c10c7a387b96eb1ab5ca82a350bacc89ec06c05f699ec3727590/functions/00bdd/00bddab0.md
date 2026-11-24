# 00bddab0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdda60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0017.md#compare-2365dfa654c8420eeab13346cf4e0a35)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a500`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a500.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0011.md#compare-c04164e1f3219a741e77ad3924f32a18)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddab0",
  "name": "<EXTERNAL>::strncpy",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d82a0d82fbf3c2b1b7012a9e595994d8ee65179c67418811b4cbfb17d70101a",
  "source_text_sha256": "4d82a0d82fbf3c2b1b7012a9e595994d8ee65179c67418811b4cbfb17d70101a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddab0",
        "00bddabf"
      ]
    ],
    "bytes_sha256": "a7af47f782b7e25cdcf356ddf5bca2734ab68a2ba5904233b369e1e22f59eb13",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00759ddc](../00759/00759ddc.md)
- [00af7838](../00af7/00af7838.md)

## 呼び出し先

- [010a5550](../010a5/010a5550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 227 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

char * strncpy(char *__dest,char *__src,size_t __n)

{
  char *pcVar1;
  
  pcVar1 = (char *)(*(code *)PTR_strncpy_00c1d610)();
  return pcVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddab0"></a> `00bddab0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddab4"></a> `00bddab4` | `11 0a 43 f9` | ldr x17,[x16, #0x610] | `FALL_THROUGH`
<a id="insn-00bddab8"></a> `00bddab8` | `10 42 18 91` | add x16,x16,#0x610 | `FALL_THROUGH`
<a id="insn-00bddabc"></a> `00bddabc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddab0`](#insn-00bddab0) 範囲 `[['00bddab0', '00bddabf']]`

## 命令位置別の参照

- [`00bddab4`](#insn-00bddab4) → `00c1d610`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddabc`](#insn-00bddabc) → [`010a5550`](../010a5/010a5550.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5550` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddab4`](#insn-00bddab4)

~~~json
{
  "source": "00bddab4",
  "target": "00c1d610",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d610",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddabc`](#insn-00bddabc)

~~~json
{
  "source": "00bddabc",
  "target": "010a5550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
