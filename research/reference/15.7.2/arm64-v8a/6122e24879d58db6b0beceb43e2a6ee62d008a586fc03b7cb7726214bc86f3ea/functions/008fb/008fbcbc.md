# 008fbcbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `008fbcbc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fb/008fbcbc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0015.md#compare-bb5a8522ea514a35265aab6a48f57e33)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008fbcbc",
  "name": "FUN_008fbcbc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "833ac304ea4627eaccc526046110fea582826232597ba87e856d8c4d2f5f47f2",
  "source_text_sha256": "833ac304ea4627eaccc526046110fea582826232597ba87e856d8c4d2f5f47f2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008fbcbc",
        "008fbce7"
      ]
    ],
    "bytes_sha256": "e60ce311f01535b7934c84813a676a78bb2acd67b36d6f1f2adf800929663b96",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006ddfb8](../006dd/006ddfb8.md)
- [00a34c84](../00a34/00a34c84.md)

## 呼び出し先

- [008f95c0](../008f9/008f95c0.md)
- [008fb5f4](../008fb/008fb5f4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 268 bytes

~~~c

void FUN_008fbcbc(char *param_1)

{
  if (*param_1 != '\0') {
    if (*(int *)(param_1 + 4) == 1) {
      FUN_008fb5f4(param_1 + 0x18);
      return;
    }
    if (*(int *)(param_1 + 4) == 0) {
      FUN_008f95c0(param_1 + 0x48);
      return;
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008fbcbc"></a> `008fbcbc` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-008fbcc0"></a> `008fbcc0` | `e8 00 00 34` | cbz w8,0x008fbcdc | `CONDITIONAL_JUMP`
<a id="insn-008fbcc4"></a> `008fbcc4` | `08 04 40 b9` | ldr w8,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-008fbcc8"></a> `008fbcc8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-008fbccc"></a> `008fbccc` | `a0 00 00 54` | b.eq 0x008fbce0 | `CONDITIONAL_JUMP`
<a id="insn-008fbcd0"></a> `008fbcd0` | `68 00 00 35` | cbnz w8,0x008fbcdc | `CONDITIONAL_JUMP`
<a id="insn-008fbcd4"></a> `008fbcd4` | `00 20 01 91` | add x0,x0,#0x48 | `FALL_THROUGH`
<a id="insn-008fbcd8"></a> `008fbcd8` | `3a f6 ff 17` | b 0x008f95c0 | `CALL_TERMINATOR`
<a id="insn-008fbcdc"></a> `008fbcdc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008fbce0"></a> `008fbce0` | `00 60 00 91` | add x0,x0,#0x18 | `FALL_THROUGH`
<a id="insn-008fbce4"></a> `008fbce4` | `44 fe ff 17` | b 0x008fb5f4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008fbcbc`](#insn-008fbcbc) 範囲 `[['008fbcbc', '008fbcc3']]`
  - `CONDITIONAL_JUMP` [`008fbcc0`](#insn-008fbcc0) → [`008fbcdc`](#insn-008fbcdc)
  - `FALL_THROUGH` [`008fbcc0`](#insn-008fbcc0) → [`008fbcc4`](#insn-008fbcc4)
- ブロック [`008fbcc4`](#insn-008fbcc4) 範囲 `[['008fbcc4', '008fbccf']]`
  - `CONDITIONAL_JUMP` [`008fbccc`](#insn-008fbccc) → [`008fbce0`](#insn-008fbce0)
  - `FALL_THROUGH` [`008fbccc`](#insn-008fbccc) → [`008fbcd0`](#insn-008fbcd0)
- ブロック [`008fbcd0`](#insn-008fbcd0) 範囲 `[['008fbcd0', '008fbcd3']]`
  - `CONDITIONAL_JUMP` [`008fbcd0`](#insn-008fbcd0) → [`008fbcdc`](#insn-008fbcdc)
  - `FALL_THROUGH` [`008fbcd0`](#insn-008fbcd0) → [`008fbcd4`](#insn-008fbcd4)
- ブロック [`008fbcd4`](#insn-008fbcd4) 範囲 `[['008fbcd4', '008fbcdb']]`
- ブロック [`008fbcdc`](#insn-008fbcdc) 範囲 `[['008fbcdc', '008fbcdf']]`
- ブロック [`008fbce0`](#insn-008fbce0) 範囲 `[['008fbce0', '008fbce7']]`

## 命令位置別の参照

- [`008fbcc0`](#insn-008fbcc0) → [`008fbcdc`](#insn-008fbcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbccc`](#insn-008fbccc) → [`008fbce0`](#insn-008fbce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbcd0`](#insn-008fbcd0) → [`008fbcdc`](#insn-008fbcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbcd8`](#insn-008fbcd8) → [`008f95c0`](../008f9/008f95c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008f95c0` · 推定シンボル `None` · 推定型 `None`
- [`008fbce4`](#insn-008fbce4) → [`008fb5f4`](008fb5f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008fb5f4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008fbcc0`](#insn-008fbcc0)

~~~json
{
  "source": "008fbcc0",
  "target": "008fbcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbccc`](#insn-008fbccc)

~~~json
{
  "source": "008fbccc",
  "target": "008fbce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbcd0`](#insn-008fbcd0)

~~~json
{
  "source": "008fbcd0",
  "target": "008fbcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbcd8`](#insn-008fbcd8)

~~~json
{
  "source": "008fbcd8",
  "target": "008f95c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbce4`](#insn-008fbce4)

~~~json
{
  "source": "008fbce4",
  "target": "008fb5f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
