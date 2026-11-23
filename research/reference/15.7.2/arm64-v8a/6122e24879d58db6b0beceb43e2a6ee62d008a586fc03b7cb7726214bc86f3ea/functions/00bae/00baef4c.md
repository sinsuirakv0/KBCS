# 00baef4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baf014`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf014.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-c4f69e7b0a0f14ac788221c9a4bcc2dc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baef4c",
  "name": "_ZNSt6__ndk18numpunctIcED1Ev",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7cec6f8788b4bdca7f80d4e0a9e2838a97ecf76a7855f614ccfde4f50273397",
  "source_text_sha256": "f7cec6f8788b4bdca7f80d4e0a9e2838a97ecf76a7855f614ccfde4f50273397",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baef4c",
        "00baef9b"
      ]
    ],
    "bytes_sha256": "ccb9b7606c76363a0b058d058033b5d113c462f19d7e4a708eda25bc7869a9c9",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1b30](../00be1/00be1b30.md)
- [00be1b40](../00be1/00be1b40.md)
- [00be1b90](../00be1/00be1b90.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb3b0](../00bdb/00bdb3b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 265 bytes

~~~c

void _ZNSt6__ndk18numpunctIcED1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk18numpunctIcEE_00c1beb8 + 0x10);
  if ((*(byte *)(param_1 + 3) & 1) != 0) {
    _ZdlPv((void *)param_1[5]);
  }
  _ZNSt6__ndk119__shared_weak_countD2Ev(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baef4c"></a> `00baef4c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baef50"></a> `00baef50` | `68 03 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00baef54"></a> `00baef54` | `08 5d 47 f9` | ldr x8,[x8, #0xeb8] | `FALL_THROUGH`
<a id="insn-00baef58"></a> `00baef58` | `09 60 40 39` | ldrb w9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baef5c"></a> `00baef5c` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00baef60"></a> `00baef60` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00baef64"></a> `00baef64` | `a9 01 00 36` | tbz w9,#0x0,0x00baef98 | `CONDITIONAL_JUMP`
<a id="insn-00baef68"></a> `00baef68` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baef6c"></a> `00baef6c` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00baef70"></a> `00baef70` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baef74"></a> `00baef74` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00baef78"></a> `00baef78` | `08 14 40 f9` | ldr x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00baef7c"></a> `00baef7c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baef80"></a> `00baef80` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00baef84"></a> `00baef84` | `f7 af 00 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00baef88"></a> `00baef88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baef8c"></a> `00baef8c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baef90"></a> `00baef90` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00baef94"></a> `00baef94` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baef98"></a> `00baef98` | `06 b1 00 14` | b 0x00bdb3b0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baef4c`](#insn-00baef4c) 範囲 `[['00baef4c', '00baef67']]`
  - `CONDITIONAL_JUMP` [`00baef64`](#insn-00baef64) → [`00baef98`](#insn-00baef98)
  - `FALL_THROUGH` [`00baef64`](#insn-00baef64) → [`00baef68`](#insn-00baef68)
- ブロック [`00baef68`](#insn-00baef68) 範囲 `[['00baef68', '00baef97']]`
  - `FALL_THROUGH` [`00baef94`](#insn-00baef94) → [`00baef98`](#insn-00baef98)
- ブロック [`00baef98`](#insn-00baef98) 範囲 `[['00baef98', '00baef9b']]`

## 命令位置別の参照

- [`00baef54`](#insn-00baef54) → `00c1beb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00baef60`](#insn-00baef60) → `00c13a78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00baef64`](#insn-00baef64) → [`00baef98`](#insn-00baef98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef6c`](#insn-00baef6c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef70`](#insn-00baef70) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef84`](#insn-00baef84) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00baef8c`](#insn-00baef8c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef90`](#insn-00baef90) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef98`](#insn-00baef98) → [`00bdb3b0`](../00bdb/00bdb3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb3b0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baef54`](#insn-00baef54)

~~~json
{
  "source": "00baef54",
  "target": "00c1beb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1beb8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00baef60`](#insn-00baef60)

~~~json
{
  "source": "00baef60",
  "target": "00c13a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13a68",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00baef64`](#insn-00baef64)

~~~json
{
  "source": "00baef64",
  "target": "00baef98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef6c`](#insn-00baef6c)

~~~json
{
  "source": "00baef6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef70`](#insn-00baef70)

~~~json
{
  "source": "00baef70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef84`](#insn-00baef84)

~~~json
{
  "source": "00baef84",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baef8c`](#insn-00baef8c)

~~~json
{
  "source": "00baef8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef90`](#insn-00baef90)

~~~json
{
  "source": "00baef90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef98`](#insn-00baef98)

~~~json
{
  "source": "00baef98",
  "target": "00bdb3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
