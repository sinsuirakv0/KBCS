# 00bdcaf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcba0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcba0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-5a81db92f487c8c9db2f6daa59029e1e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcaf0",
  "name": "_ZN5Botan27Certificate_Store_In_Memory7add_crlENSt6__ndk110shared_ptrIKNS_8X509_CRLEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c0235d80fb16a804236e40ba739e3f1640535d4d2e2a1917a3daa84e3141a5c3",
  "source_text_sha256": "c0235d80fb16a804236e40ba739e3f1640535d4d2e2a1917a3daa84e3141a5c3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcaf0",
        "00bdcaff"
      ]
    ],
    "bytes_sha256": "450a3c5ff10842374bb751804a87f8ac94751ea01a306bf3bd9096646ba5bd43",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004df5b0](../004df/004df5b0.md)

## 呼び出し先

- [004df724](../004df/004df724.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 239 bytes

~~~c

void _ZN5Botan27Certificate_Store_In_Memory7add_crlENSt6__ndk110shared_ptrIKNS_8X509_CRLEEE(void)

{
  (*(code *)
    PTR__ZN5Botan27Certificate_Store_In_Memory7add_crlENSt6__ndk110shared_ptrIKNS_8X509_CRLEEE_00c1cdb0
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcaf0"></a> `00bdcaf0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcaf4"></a> `00bdcaf4` | `11 da 46 f9` | ldr x17,[x16, #0xdb0] | `FALL_THROUGH`
<a id="insn-00bdcaf8"></a> `00bdcaf8` | `10 c2 36 91` | add x16,x16,#0xdb0 | `FALL_THROUGH`
<a id="insn-00bdcafc"></a> `00bdcafc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcaf0`](#insn-00bdcaf0) 範囲 `[['00bdcaf0', '00bdcaff']]`

## 命令位置別の参照

- [`00bdcaf4`](#insn-00bdcaf4) → `00c1cdb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcafc`](#insn-00bdcafc) → [`004df724`](../004df/004df724.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004df724` · 推定シンボル `_ZN5Botan27Certificate_Store_In_Memory7add_crlENSt6__ndk110shared_ptrIKNS_8X509_CRLEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcaf4`](#insn-00bdcaf4)

~~~json
{
  "source": "00bdcaf4",
  "target": "00c1cdb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cdb0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcafc`](#insn-00bdcafc)

~~~json
{
  "source": "00bdcafc",
  "target": "004df724",
  "target_space": "ram",
  "resolution": "function"
}
~~~
