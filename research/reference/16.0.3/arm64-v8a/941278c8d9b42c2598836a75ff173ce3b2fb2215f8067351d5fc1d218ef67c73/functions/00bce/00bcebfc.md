# 00bcebfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcdc08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-fd31ab5bafa58aca2a0616f21c3ec623)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcebfc",
  "name": "_ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e39dd7aee7500a646f35854bb33ec343c7150838a9b3fe209f2b5275559c6a6c",
  "source_text_sha256": "e39dd7aee7500a646f35854bb33ec343c7150838a9b3fe209f2b5275559c6a6c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcebfc",
        "00bcec3b"
      ]
    ],
    "bytes_sha256": "88d3e1efdccdd0fa4fec2ac8dce6fb3ecc792303705aa79bfd5e3e1d903f7b05",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5ea90](../00c5e/00c5ea90.md)
- [00c5ecd0](../00c5e/00c5ecd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 635 bytes

~~~c

void _ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl
               (undefined8 param_1,undefined8 param_2,long param_3)

{
  _ZN8firebase5Mutex7AcquireEv(param_3 + 700);
                    /* try { // try from 00bcec18 to 00ccec1f has its CatchHandler @ 00bcfa80 */
  *(undefined1 *)(param_3 + 0x2b8) = 0;
                    /* try { // try from 00bcec20 to 00ccedc3 has its CatchHandler @ 00bcd634 */
  _ZN8firebase5Mutex7ReleaseEv(param_3 + 700);
  _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE(param_3);
  _ZN8firebase4auth22NotifyIdTokenListenersEPNS0_8AuthDataE(param_3);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcebfc"></a> `00bcebfc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcec00"></a> `00bcec00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcec04"></a> `00bcec04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcec08"></a> `00bcec08` | `54 f0 0a 91` | add x20,x2,#0x2bc | `FALL_THROUGH`
<a id="insn-00bcec0c"></a> `00bcec0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcec10"></a> `00bcec10` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bcec14"></a> `00bcec14` | `a3 33 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec18"></a> `00bcec18` | `7f e2 0a 39` | strb wzr,[x19, #0x2b8] | `FALL_THROUGH`
<a id="insn-00bcec1c"></a> `00bcec1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcec20"></a> `00bcec20` | `a4 33 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec24"></a> `00bcec24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcec28"></a> `00bcec28` | `2a 40 02 94` | bl 0x00c5ecd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec2c"></a> `00bcec2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcec30"></a> `00bcec30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcec34"></a> `00bcec34` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcec38"></a> `00bcec38` | `96 3f 02 14` | b 0x00c5ea90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcebfc`](#insn-00bcebfc) 範囲 `[['00bcebfc', '00bcec17']]`
  - `FALL_THROUGH` [`00bcec14`](#insn-00bcec14) → [`00bcec18`](#insn-00bcec18)
- ブロック [`00bcec18`](#insn-00bcec18) 範囲 `[['00bcec18', '00bcec1f']]`
  - `FALL_THROUGH` [`00bcec1c`](#insn-00bcec1c) → [`00bcec20`](#insn-00bcec20)
- ブロック [`00bcec20`](#insn-00bcec20) 範囲 `[['00bcec20', '00bcec3b']]`

## 命令位置別の参照

- [`00bcebfc`](#insn-00bcebfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec00`](#insn-00bcec00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec14`](#insn-00bcec14) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bcec20`](#insn-00bcec20) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bcec28`](#insn-00bcec28) → [`00c5ecd0`](../00c5e/00c5ecd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ecd0` · 推定シンボル `None` · 推定型 `None`
- [`00bcec2c`](#insn-00bcec2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec38`](#insn-00bcec38) → [`00c5ea90`](../00c5e/00c5ea90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ea90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcebfc`](#insn-00bcebfc)

~~~json
{
  "source": "00bcebfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec00`](#insn-00bcec00)

~~~json
{
  "source": "00bcec00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec14`](#insn-00bcec14)

~~~json
{
  "source": "00bcec14",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec20`](#insn-00bcec20)

~~~json
{
  "source": "00bcec20",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec28`](#insn-00bcec28)

~~~json
{
  "source": "00bcec28",
  "target": "00c5ecd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec2c`](#insn-00bcec2c)

~~~json
{
  "source": "00bcec2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec38`](#insn-00bcec38)

~~~json
{
  "source": "00bcec38",
  "target": "00c5ea90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
