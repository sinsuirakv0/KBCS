# 00befcac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00befc10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-3320b15c656edb1728bb7306dab10a74)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf0ca0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0ca0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0037.md#compare-a7e2e334ef28575430a17719dd92a284)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befcac",
  "name": "_ZSt17rethrow_exceptionSt13exception_ptr",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d153d160b8592e84431cf7fcd932e340fb1c58be0e2bca67c165e5d3c4cbc5fd",
  "source_text_sha256": "d153d160b8592e84431cf7fcd932e340fb1c58be0e2bca67c165e5d3c4cbc5fd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befcac",
        "00befcc3"
      ]
    ],
    "bytes_sha256": "36055e140408d78f250059f01ca1b616b5ee4f63805ee0023ebd72303905c797",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58590](../00c58/00c58590.md)

## 呼び出し先

- [00c580f0](../00c58/00c580f0.md)
- [00c5e030](../00c5e/00c5e030.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 202 bytes

~~~c

void _ZSt17rethrow_exceptionSt13exception_ptr(undefined8 *param_1)

{
  __cxa_rethrow_primary_exception(*param_1);
                    /* WARNING: Subroutine does not return */
  _ZSt9terminatev();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befcac"></a> `00befcac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00befcb0"></a> `00befcb0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00befcb4"></a> `00befcb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00befcb8"></a> `00befcb8` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00befcbc"></a> `00befcbc` | `dd b8 01 94` | bl 0x00c5e030 | `UNCONDITIONAL_CALL`
<a id="insn-00befcc0"></a> `00befcc0` | `0c a1 01 94` | bl 0x00c580f0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befcac`](#insn-00befcac) 範囲 `[['00befcac', '00befcc3']]`

## 命令位置別の参照

- [`00befcb0`](#insn-00befcb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befcbc`](#insn-00befcbc) → [`00c5e030`](../00c5e/00c5e030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e030` · 推定シンボル `None` · 推定型 `None`
- [`00befcc0`](#insn-00befcc0) → [`00c580f0`](../00c58/00c580f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580f0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befcb0`](#insn-00befcb0)

~~~json
{
  "source": "00befcb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befcbc`](#insn-00befcbc)

~~~json
{
  "source": "00befcbc",
  "target": "00c5e030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befcc0`](#insn-00befcc0)

~~~json
{
  "source": "00befcc0",
  "target": "00c580f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
