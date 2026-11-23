# 00bdcae0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcb90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-61cd238dc4ad407246843bad4f67902d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcae0",
  "name": "_ZNK5Botan27Certificate_Store_In_Memory14find_all_certsERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a038b5b87a63262006f54679497e6ea8ec24b3340253acadb1db0ccbaadad148",
  "source_text_sha256": "a038b5b87a63262006f54679497e6ea8ec24b3340253acadb1db0ccbaadad148",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcae0",
        "00bdcaef"
      ]
    ],
    "bytes_sha256": "dedc1350e3bc912e9cf95a3ba45d8b129113542ebd3bfbb4d1df322542776c95",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00506ee0](../00506/00506ee0.md)

## 呼び出し先

- [004ded14](../004de/004ded14.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 305 bytes

~~~c

void _ZNK5Botan27Certificate_Store_In_Memory14find_all_certsERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE
               (void)

{
  (*(code *)
    PTR__ZNK5Botan27Certificate_Store_In_Memory14find_all_certsERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE_00c1cda8
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcae0"></a> `00bdcae0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcae4"></a> `00bdcae4` | `11 d6 46 f9` | ldr x17,[x16, #0xda8] | `FALL_THROUGH`
<a id="insn-00bdcae8"></a> `00bdcae8` | `10 a2 36 91` | add x16,x16,#0xda8 | `FALL_THROUGH`
<a id="insn-00bdcaec"></a> `00bdcaec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcae0`](#insn-00bdcae0) 範囲 `[['00bdcae0', '00bdcaef']]`

## 命令位置別の参照

- [`00bdcae4`](#insn-00bdcae4) → `00c1cda8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcaec`](#insn-00bdcaec) → [`004ded14`](../004de/004ded14.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004ded14` · 推定シンボル `_ZNK5Botan27Certificate_Store_In_Memory14find_all_certsERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcae4`](#insn-00bdcae4)

~~~json
{
  "source": "00bdcae4",
  "target": "00c1cda8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cda8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcaec`](#insn-00bdcaec)

~~~json
{
  "source": "00bdcaec",
  "target": "004ded14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
