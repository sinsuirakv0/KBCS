# 00bdddb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdde60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-d1f1493013584b5f43ca1d135104775e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdddb0",
  "name": "_ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99bf797bfb1f2c3e9a1596dc7e779faedf21477ca154aa7b0e3e55288a6ceb33",
  "source_text_sha256": "99bf797bfb1f2c3e9a1596dc7e779faedf21477ca154aa7b0e3e55288a6ceb33",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdddb0",
        "00bdddbf"
      ]
    ],
    "bytes_sha256": "e4dacf00d26d76c8fb9210e37f87b4e9d14f7698de7909bfd4bc508e83f9f3e6",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae01e4](../00ae0/00ae01e4.md)
- [00b49e24](../00b49/00b49e24.md)
- [00b4eba8](../00b4e/00b4eba8.md)
- [00b4fee4](../00b4f/00b4fee4.md)
- [00b5220c](../00b52/00b5220c.md)
- [00b55564](../00b55/00b55564.md)
- [00b562c4](../00b56/00b562c4.md)
- [00b5bc88](../00b5b/00b5bc88.md)
- [00b5beb0](../00b5b/00b5beb0.md)
- [00b5c3f0](../00b5c/00b5c3f0.md)
- [00b5c4e8](../00b5c/00b5c4e8.md)
- [00b5c5e0](../00b5c/00b5c5e0.md)
- [00b71cf4](../00b71/00b71cf4.md)

## 呼び出し先

- [00ae03a0](../00ae0/00ae03a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 189 bytes

~~~c

void _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(void)

{
  (*(code *)PTR__ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv_00c1d710)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdddb0"></a> `00bdddb0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdddb4"></a> `00bdddb4` | `11 8a 43 f9` | ldr x17,[x16, #0x710] | `FALL_THROUGH`
<a id="insn-00bdddb8"></a> `00bdddb8` | `10 42 1c 91` | add x16,x16,#0x710 | `FALL_THROUGH`
<a id="insn-00bdddbc"></a> `00bdddbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdddb0`](#insn-00bdddb0) 範囲 `[['00bdddb0', '00bdddbf']]`

## 命令位置別の参照

- [`00bdddb4`](#insn-00bdddb4) → `00c1d710`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdddbc`](#insn-00bdddbc) → [`00ae03a0`](../00ae0/00ae03a0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae03a0` · 推定シンボル `_ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdddb4`](#insn-00bdddb4)

~~~json
{
  "source": "00bdddb4",
  "target": "00c1d710",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d710",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdddbc`](#insn-00bdddbc)

~~~json
{
  "source": "00bdddbc",
  "target": "00ae03a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
