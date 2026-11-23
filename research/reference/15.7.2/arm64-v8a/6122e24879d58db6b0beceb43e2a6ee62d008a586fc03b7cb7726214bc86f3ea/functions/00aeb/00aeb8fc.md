# 00aeb8fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeb9c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb9c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-fd265592365728f8410f1139024a1f11)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeb8fc",
  "name": "_ZN8firebase4util8iterable14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "24a34cb62d7390b0b904c3e7ce2c4255ca15e14ea200d03aa0acf5c0a96b13f8",
  "source_text_sha256": "24a34cb62d7390b0b904c3e7ce2c4255ca15e14ea200d03aa0acf5c0a96b13f8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeb8fc",
        "00aeb96b"
      ]
    ],
    "bytes_sha256": "c0648977f8cf5b3de657410481604bab6a92b5084d4877ba014a13ddec205940",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Iterable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 807 bytes

~~~c

void _ZN8firebase4util8iterable14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00aeb914 to 00beb92b has its CatchHandler @ 00af18e0 */
  if (DAT_010a07d8 == 0) {
                    /* try { // try from 00aeb92c to 00beb93f has its CatchHandler @ 00af18c4 */
    DAT_010a07d8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Iterable",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a07d8,&PTR_s_iterator_00c10378,1,&DAT_010a07e8,"java/lang/Iterable");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeb8fc"></a> `00aeb8fc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeb900"></a> `00aeb900` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb904"></a> `00aeb904` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeb908"></a> `00aeb908` | `b4 2d 00 b0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeb90c"></a> `00aeb90c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aeb910"></a> `00aeb910` | `81 ee 43 f9` | ldr x1,[x20, #0x7d8] | `FALL_THROUGH`
<a id="insn-00aeb914"></a> `00aeb914` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeb918"></a> `00aeb918` | `41 01 00 b5` | cbnz x1,0x00aeb940 | `CONDITIONAL_JUMP`
<a id="insn-00aeb91c"></a> `00aeb91c` | `23 bd ff b0` | adrp x3,0x290000 | `FALL_THROUGH`
<a id="insn-00aeb920"></a> `00aeb920` | `63 c8 0d 91` | add x3,x3,#0x372 | `FALL_THROUGH`
<a id="insn-00aeb924"></a> `00aeb924` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeb928"></a> `00aeb928` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aeb92c"></a> `00aeb92c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeb930"></a> `00aeb930` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeb934"></a> `00aeb934` | `97 c9 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeb938"></a> `00aeb938` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aeb93c"></a> `00aeb93c` | `80 ee 03 f9` | str x0,[x20, #0x7d8] | `FALL_THROUGH`
<a id="insn-00aeb940"></a> `00aeb940` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb944"></a> `00aeb944` | `22 09 00 b0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aeb948"></a> `00aeb948` | `a4 2d 00 b0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeb94c"></a> `00aeb94c` | `25 bd ff b0` | adrp x5,0x290000 | `FALL_THROUGH`
<a id="insn-00aeb950"></a> `00aeb950` | `42 e0 0d 91` | add x2,x2,#0x378 | `FALL_THROUGH`
<a id="insn-00aeb954"></a> `00aeb954` | `84 a0 1f 91` | add x4,x4,#0x7e8 | `FALL_THROUGH`
<a id="insn-00aeb958"></a> `00aeb958` | `a5 c8 0d 91` | add x5,x5,#0x372 | `FALL_THROUGH`
<a id="insn-00aeb95c"></a> `00aeb95c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aeb960"></a> `00aeb960` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeb964"></a> `00aeb964` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeb968"></a> `00aeb968` | `92 c9 03 14` | b 0x00bddfb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeb8fc`](#insn-00aeb8fc) 範囲 `[['00aeb8fc', '00aeb913']]`
  - `FALL_THROUGH` [`00aeb910`](#insn-00aeb910) → [`00aeb914`](#insn-00aeb914)
- ブロック [`00aeb914`](#insn-00aeb914) 範囲 `[['00aeb914', '00aeb91b']]`
  - `CONDITIONAL_JUMP` [`00aeb918`](#insn-00aeb918) → [`00aeb940`](#insn-00aeb940)
  - `FALL_THROUGH` [`00aeb918`](#insn-00aeb918) → [`00aeb91c`](#insn-00aeb91c)
- ブロック [`00aeb91c`](#insn-00aeb91c) 範囲 `[['00aeb91c', '00aeb92b']]`
  - `FALL_THROUGH` [`00aeb928`](#insn-00aeb928) → [`00aeb92c`](#insn-00aeb92c)
- ブロック [`00aeb92c`](#insn-00aeb92c) 範囲 `[['00aeb92c', '00aeb93f']]`
  - `FALL_THROUGH` [`00aeb93c`](#insn-00aeb93c) → [`00aeb940`](#insn-00aeb940)
- ブロック [`00aeb940`](#insn-00aeb940) 範囲 `[['00aeb940', '00aeb96b']]`

## 命令位置別の参照

- [`00aeb8fc`](#insn-00aeb8fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb900`](#insn-00aeb900) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb910`](#insn-00aeb910) → `010a07d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeb918`](#insn-00aeb918) → [`00aeb940`](#insn-00aeb940) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb920`](#insn-00aeb920) → `00290372`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeb934`](#insn-00aeb934) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aeb93c`](#insn-00aeb93c) → `010a07d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeb940`](#insn-00aeb940) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb950`](#insn-00aeb950) → `00c10378`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aeb954`](#insn-00aeb954) → `010a07e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb958`](#insn-00aeb958) → `00290372`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeb968`](#insn-00aeb968) → [`00bddfb0`](../00bdd/00bddfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeb8fc`](#insn-00aeb8fc)

~~~json
{
  "source": "00aeb8fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb900`](#insn-00aeb900)

~~~json
{
  "source": "00aeb900",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb910`](#insn-00aeb910)

~~~json
{
  "source": "00aeb910",
  "target": "010a07d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb918`](#insn-00aeb918)

~~~json
{
  "source": "00aeb918",
  "target": "00aeb940",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb920`](#insn-00aeb920)

~~~json
{
  "source": "00aeb920",
  "target": "00290372",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290372",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4974657261626c6500",
  "capture_start": "00290372",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeb934`](#insn-00aeb934)

~~~json
{
  "source": "00aeb934",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeb93c`](#insn-00aeb93c)

~~~json
{
  "source": "00aeb93c",
  "target": "010a07d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb940`](#insn-00aeb940)

~~~json
{
  "source": "00aeb940",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb950`](#insn-00aeb950)

~~~json
{
  "source": "00aeb950",
  "target": "00c10378",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10378",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeb954`](#insn-00aeb954)

~~~json
{
  "source": "00aeb954",
  "target": "010a07e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb958`](#insn-00aeb958)

~~~json
{
  "source": "00aeb958",
  "target": "00290372",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290372",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4974657261626c6500",
  "capture_start": "00290372",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeb968`](#insn-00aeb968)

~~~json
{
  "source": "00aeb968",
  "target": "00bddfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
