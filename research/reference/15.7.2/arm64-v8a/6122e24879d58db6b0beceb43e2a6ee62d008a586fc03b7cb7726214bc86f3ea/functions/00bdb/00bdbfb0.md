# 00bdbfb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdc060`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc060.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-c6bc0f35b2584e62dd0b194ed8ed3e2c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbfb0",
  "name": "_ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC1Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f89399fe22f212667e19f357f98279eb4a65347d4c717b5b3a911a079b4dcfe6",
  "source_text_sha256": "f89399fe22f212667e19f357f98279eb4a65347d4c717b5b3a911a079b4dcfe6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbfb0",
        "00bdbfbf"
      ]
    ],
    "bytes_sha256": "258f9a0a1d034fff33871e67075fbb231ab59ec2fcb1cd17ab9d6498b0423b17",
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

## 呼び出し先

- [00b88710](../00b88/00b88710.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 167 bytes

~~~c

void _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC1Ev(void)

{
  (*(code *)PTR__ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC1Ev_00c1c810)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbfb0"></a> `00bdbfb0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbfb4"></a> `00bdbfb4` | `11 0a 44 f9` | ldr x17,[x16, #0x810] | `FALL_THROUGH`
<a id="insn-00bdbfb8"></a> `00bdbfb8` | `10 42 20 91` | add x16,x16,#0x810 | `FALL_THROUGH`
<a id="insn-00bdbfbc"></a> `00bdbfbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbfb0`](#insn-00bdbfb0) 範囲 `[['00bdbfb0', '00bdbfbf']]`

## 命令位置別の参照

- [`00bdbfb4`](#insn-00bdbfb4) → `00c1c810`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbfbc`](#insn-00bdbfbc) → [`00b88710`](../00b88/00b88710.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b88710` · 推定シンボル `_ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC1Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbfb4`](#insn-00bdbfb4)

~~~json
{
  "source": "00bdbfb4",
  "target": "00c1c810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c810",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbfbc`](#insn-00bdbfbc)

~~~json
{
  "source": "00bdbfbc",
  "target": "00b88710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
