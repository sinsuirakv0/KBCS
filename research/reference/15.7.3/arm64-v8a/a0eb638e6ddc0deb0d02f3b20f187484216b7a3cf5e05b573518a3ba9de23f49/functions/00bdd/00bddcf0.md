# 00bddcf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddc40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-9e8eba9009910d930bfef095fcdf57eb)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddd40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-b72a413e38c7c3b4c1589dbff9019edd)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddcf0",
  "name": "_ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "457c2f52339952835e4d1a39d7aadefbbbe0ad6669005b94c0dbfc0fd8afa583",
  "source_text_sha256": "457c2f52339952835e4d1a39d7aadefbbbe0ad6669005b94c0dbfc0fd8afa583",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddcf0",
        "00bddcff"
      ]
    ],
    "bytes_sha256": "7dca9241a8f05d1753a0a896503943c5d803796cdba1586668f12fe903e16549",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae0f70](../00ae0/00ae0f70.md)
- [00af5a60](../00af5/00af5a60.md)
- [00b061ec](../00b06/00b061ec.md)
- [00b06ce0](../00b06/00b06ce0.md)
- [00b07f84](../00b07/00b07f84.md)
- [00b0dc70](../00b0d/00b0dc70.md)
- [00b0df30](../00b0d/00b0df30.md)
- [00b4c480](../00b4c/00b4c480.md)
- [00b54af4](../00b54/00b54af4.md)
- [00b5dce8](../00b5d/00b5dce8.md)
- [00b5e148](../00b5e/00b5e148.md)
- [00b69ab8](../00b69/00b69ab8.md)
- [00b69f14](../00b69/00b69f14.md)
- [00b6a060](../00b6a/00b6a060.md)
- [00b6a1ac](../00b6a/00b6a1ac.md)
- [00b6a350](../00b6a/00b6a350.md)
- [00b6a49c](../00b6a/00b6a49c.md)
- [00b6a620](../00b6a/00b6a620.md)
- [00b6a7e4](../00b6a/00b6a7e4.md)
- [00b6b64c](../00b6b/00b6b64c.md)
- [00b6b7c8](../00b6b/00b6b7c8.md)
- [00b6c2cc](../00b6c/00b6c2cc.md)

## 呼び出し先

- [00ae1264](../00ae1/00ae1264.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 177 bytes

~~~c

void _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz(void)

{
  (*(code *)PTR__ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz_00c1d708)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddcf0"></a> `00bddcf0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddcf4"></a> `00bddcf4` | `11 86 43 f9` | ldr x17,[x16, #0x708] | `FALL_THROUGH`
<a id="insn-00bddcf8"></a> `00bddcf8` | `10 22 1c 91` | add x16,x16,#0x708 | `FALL_THROUGH`
<a id="insn-00bddcfc"></a> `00bddcfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddcf0`](#insn-00bddcf0) 範囲 `[['00bddcf0', '00bddcff']]`

## 命令位置別の参照

- [`00bddcf4`](#insn-00bddcf4) → `00c1d708`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddcfc`](#insn-00bddcfc) → [`00ae1264`](../00ae1/00ae1264.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae1264` · 推定シンボル `_ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddcf4`](#insn-00bddcf4)

~~~json
{
  "source": "00bddcf4",
  "target": "00c1d708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d708",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddcfc`](#insn-00bddcfc)

~~~json
{
  "source": "00bddcfc",
  "target": "00ae1264",
  "target_space": "ram",
  "resolution": "function"
}
~~~
