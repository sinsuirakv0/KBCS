# 00bdbfc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdc070`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc070.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-98ddc9fe76e119eb70d040d776477ce0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbfc0",
  "name": "_ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4openEPKcj",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cb1273fbfe37c1c0fc15c8ed1a7f182d9a17b4f05e723f4e4425d058518330dd",
  "source_text_sha256": "cb1273fbfe37c1c0fc15c8ed1a7f182d9a17b4f05e723f4e4425d058518330dd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbfc0",
        "00bdbfcf"
      ]
    ],
    "bytes_sha256": "133378d0bfa1ac8f92b0fe722aeb37430ebd9db6ca018ce678703c1a5654137d",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004a36fc](../004a3/004a36fc.md)
- [004d7338](../004d7/004d7338.md)
- [00b46650](../00b46/00b46650.md)
- [00b46e18](../00b46/00b46e18.md)

## 呼び出し先

- [00b48960](../00b48/00b48960.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 179 bytes

~~~c

void _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4openEPKcj(void)

{
  (*(code *)PTR__ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4openEPKcj_00c1c818)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbfc0"></a> `00bdbfc0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbfc4"></a> `00bdbfc4` | `11 0e 44 f9` | ldr x17,[x16, #0x818] | `FALL_THROUGH`
<a id="insn-00bdbfc8"></a> `00bdbfc8` | `10 62 20 91` | add x16,x16,#0x818 | `FALL_THROUGH`
<a id="insn-00bdbfcc"></a> `00bdbfcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbfc0`](#insn-00bdbfc0) 範囲 `[['00bdbfc0', '00bdbfcf']]`

## 命令位置別の参照

- [`00bdbfc4`](#insn-00bdbfc4) → `00c1c818`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbfcc`](#insn-00bdbfcc) → [`00b48960`](../00b48/00b48960.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b48960` · 推定シンボル `_ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4openEPKcj` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbfc4`](#insn-00bdbfc4)

~~~json
{
  "source": "00bdbfc4",
  "target": "00c1c818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c818",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbfcc`](#insn-00bdbfcc)

~~~json
{
  "source": "00bdbfcc",
  "target": "00b48960",
  "target_space": "ram",
  "resolution": "function"
}
~~~
