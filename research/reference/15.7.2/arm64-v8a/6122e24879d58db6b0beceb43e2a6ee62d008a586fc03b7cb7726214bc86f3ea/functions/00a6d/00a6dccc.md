# 00a6dccc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a6dccc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6dccc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0020.md#compare-140cb9e4ecfa9f886e84a6e1efa18a18)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6dccc",
  "name": "FUN_00a6dccc",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0c7d514cea52e14a368d9f9e179c04ce973ea6e439527e75dcd0cd2518fe85f2",
  "source_text_sha256": "0c7d514cea52e14a368d9f9e179c04ce973ea6e439527e75dcd0cd2518fe85f2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a6dccc",
        "00a6dd07"
      ]
    ],
    "bytes_sha256": "d740f6e81e44900d593a8109a669a4af56062ffa417116484b6ee3dcab302ba3",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00707eec](../00707/00707eec.md)
- [00900f40](../00900/00900f40.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 454 bytes

~~~c

int FUN_00a6dccc(long param_1)

{
  long lVar1;
  int iVar2;
  long lVar3;
  
  if (*(long *)(param_1 + 0x30) == 0) {
    iVar2 = 0;
  }
  else {
    iVar2 = 0;
    lVar1 = *(long *)(param_1 + 0x30);
    lVar3 = param_1;
    do {
      param_1 = lVar1;
      iVar2 = *(int *)(lVar3 + 8) + iVar2;
      lVar1 = *(long *)(param_1 + 0x30);
      lVar3 = param_1;
    } while (*(long *)(param_1 + 0x30) != 0);
  }
  return *(int *)(param_1 + 8) + iVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a6dccc"></a> `00a6dccc` | `09 18 40 f9` | ldr x9,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00a6dcd0"></a> `00a6dcd0` | `49 01 00 b4` | cbz x9,0x00a6dcf8 | `CONDITIONAL_JUMP`
<a id="insn-00a6dcd4"></a> `00a6dcd4` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00a6dcd8"></a> `00a6dcd8` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00a6dcdc"></a> `00a6dcdc` | `4a 09 40 b9` | ldr w10,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00a6dce0"></a> `00a6dce0` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00a6dce4"></a> `00a6dce4` | `29 19 40 f9` | ldr x9,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00a6dce8"></a> `00a6dce8` | `48 01 08 0b` | add w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00a6dcec"></a> `00a6dcec` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00a6dcf0"></a> `00a6dcf0` | `69 ff ff b5` | cbnz x9,0x00a6dcdc | `CONDITIONAL_JUMP`
<a id="insn-00a6dcf4"></a> `00a6dcf4` | `02 00 00 14` | b 0x00a6dcfc | `UNCONDITIONAL_JUMP`
<a id="insn-00a6dcf8"></a> `00a6dcf8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00a6dcfc"></a> `00a6dcfc` | `09 08 40 b9` | ldr w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a6dd00"></a> `00a6dd00` | `20 01 08 0b` | add w0,w9,w8 | `FALL_THROUGH`
<a id="insn-00a6dd04"></a> `00a6dd04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a6dccc`](#insn-00a6dccc) 範囲 `[['00a6dccc', '00a6dcd3']]`
  - `CONDITIONAL_JUMP` [`00a6dcd0`](#insn-00a6dcd0) → [`00a6dcf8`](#insn-00a6dcf8)
  - `FALL_THROUGH` [`00a6dcd0`](#insn-00a6dcd0) → [`00a6dcd4`](#insn-00a6dcd4)
- ブロック [`00a6dcd4`](#insn-00a6dcd4) 範囲 `[['00a6dcd4', '00a6dcdb']]`
  - `FALL_THROUGH` [`00a6dcd8`](#insn-00a6dcd8) → [`00a6dcdc`](#insn-00a6dcdc)
- ブロック [`00a6dcdc`](#insn-00a6dcdc) 範囲 `[['00a6dcdc', '00a6dcf3']]`
  - `CONDITIONAL_JUMP` [`00a6dcf0`](#insn-00a6dcf0) → [`00a6dcdc`](#insn-00a6dcdc)
  - `FALL_THROUGH` [`00a6dcf0`](#insn-00a6dcf0) → [`00a6dcf4`](#insn-00a6dcf4)
- ブロック [`00a6dcf4`](#insn-00a6dcf4) 範囲 `[['00a6dcf4', '00a6dcf7']]`
  - `UNCONDITIONAL_JUMP` [`00a6dcf4`](#insn-00a6dcf4) → [`00a6dcfc`](#insn-00a6dcfc)
- ブロック [`00a6dcf8`](#insn-00a6dcf8) 範囲 `[['00a6dcf8', '00a6dcfb']]`
  - `FALL_THROUGH` [`00a6dcf8`](#insn-00a6dcf8) → [`00a6dcfc`](#insn-00a6dcfc)
- ブロック [`00a6dcfc`](#insn-00a6dcfc) 範囲 `[['00a6dcfc', '00a6dd07']]`

## 命令位置別の参照

- [`00a6dcd0`](#insn-00a6dcd0) → [`00a6dcf8`](#insn-00a6dcf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dcf0`](#insn-00a6dcf0) → [`00a6dcdc`](#insn-00a6dcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dcf4`](#insn-00a6dcf4) → [`00a6dcfc`](#insn-00a6dcfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a6dcd0`](#insn-00a6dcd0)

~~~json
{
  "source": "00a6dcd0",
  "target": "00a6dcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dcf0`](#insn-00a6dcf0)

~~~json
{
  "source": "00a6dcf0",
  "target": "00a6dcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dcf4`](#insn-00a6dcf4)

~~~json
{
  "source": "00a6dcf4",
  "target": "00a6dcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
