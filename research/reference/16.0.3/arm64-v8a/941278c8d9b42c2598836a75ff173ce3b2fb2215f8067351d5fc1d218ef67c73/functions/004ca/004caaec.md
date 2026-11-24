# 004caaec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004ca7cc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004ca7cc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/detail_skipped-0002.md#compare-fedeaedeaf2b8e58f78f15978b47d77c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004caaec",
  "name": "_ZThn80_NK5Botan11SecureQueue11end_of_dataEv",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e142d582f5a3b4408e052b935f435a29bdf14db0b3651618d0978a08ecee2839",
  "source_text_sha256": "e142d582f5a3b4408e052b935f435a29bdf14db0b3651618d0978a08ecee2839",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004caaec",
        "004cab1f"
      ]
    ],
    "bytes_sha256": "aeb72e63af7670b9a6c8af230022aeec1e2a70705fb60f00cc646b066ee87110",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 438 bytes

~~~c

bool _ZThn80_NK5Botan11SecureQueue11end_of_dataEv(long param_1)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  
  plVar3 = *(long **)(param_1 + 0x10);
  if (plVar3 != (long *)0x0) {
    lVar4 = 0;
    do {
      plVar1 = plVar3 + 4;
      plVar2 = plVar3 + 5;
      plVar3 = (long *)*plVar3;
      lVar4 = (*plVar2 + lVar4) - *plVar1;
    } while (plVar3 != (long *)0x0);
    return lVar4 == 0;
  }
  return true;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004caaec"></a> `004caaec` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004caaf0"></a> `004caaf0` | `48 01 00 b4` | cbz x8,0x004cab18 | `CONDITIONAL_JUMP`
<a id="insn-004caaf4"></a> `004caaf4` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-004caaf8"></a> `004caaf8` | `0b 29 42 a9` | ldp x11,x10,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-004caafc"></a> `004caafc` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-004cab00"></a> `004cab00` | `49 01 09 8b` | add x9,x10,x9 | `FALL_THROUGH`
<a id="insn-004cab04"></a> `004cab04` | `29 01 0b cb` | sub x9,x9,x11 | `FALL_THROUGH`
<a id="insn-004cab08"></a> `004cab08` | `88 ff ff b5` | cbnz x8,0x004caaf8 | `CONDITIONAL_JUMP`
<a id="insn-004cab0c"></a> `004cab0c` | `3f 01 00 f1` | cmp x9,#0x0 | `FALL_THROUGH`
<a id="insn-004cab10"></a> `004cab10` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-004cab14"></a> `004cab14` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004cab18"></a> `004cab18` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-004cab1c"></a> `004cab1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004caaec`](#insn-004caaec) 範囲 `[['004caaec', '004caaf3']]`
  - `CONDITIONAL_JUMP` [`004caaf0`](#insn-004caaf0) → [`004cab18`](#insn-004cab18)
  - `FALL_THROUGH` [`004caaf0`](#insn-004caaf0) → [`004caaf4`](#insn-004caaf4)
- ブロック [`004caaf4`](#insn-004caaf4) 範囲 `[['004caaf4', '004caaf7']]`
  - `FALL_THROUGH` [`004caaf4`](#insn-004caaf4) → [`004caaf8`](#insn-004caaf8)
- ブロック [`004caaf8`](#insn-004caaf8) 範囲 `[['004caaf8', '004cab0b']]`
  - `CONDITIONAL_JUMP` [`004cab08`](#insn-004cab08) → [`004caaf8`](#insn-004caaf8)
  - `FALL_THROUGH` [`004cab08`](#insn-004cab08) → [`004cab0c`](#insn-004cab0c)
- ブロック [`004cab0c`](#insn-004cab0c) 範囲 `[['004cab0c', '004cab17']]`
- ブロック [`004cab18`](#insn-004cab18) 範囲 `[['004cab18', '004cab1f']]`

## 命令位置別の参照

- [`004caaf0`](#insn-004caaf0) → [`004cab18`](#insn-004cab18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cab08`](#insn-004cab08) → [`004caaf8`](#insn-004caaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004caaf0`](#insn-004caaf0)

~~~json
{
  "source": "004caaf0",
  "target": "004cab18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cab08`](#insn-004cab08)

~~~json
{
  "source": "004cab08",
  "target": "004caaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
