# 00bda8fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bda4d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda4d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-6e72bdb790d5df05a5cee57af4c5f114)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bda998`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda998.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-5769fff52042665a134417717b7df6f1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bda8fc",
  "name": "_ZN8firebase4auth17PhoneAuthProviderD1Ev",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a16ac5707c15159dea4669b75def13b653c6450e518ac3f22aba750f0d9772f3",
  "source_text_sha256": "a16ac5707c15159dea4669b75def13b653c6450e518ac3f22aba750f0d9772f3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bda8fc",
        "00bda967"
      ]
    ],
    "bytes_sha256": "9d4a19e603fd1ac3151d2f6fb03313ad40fdb9fd9d9722d7b131550f19425eb7",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5d9c0](../00c5d/00c5d9c0.md)

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b260](../00c5b/00c5b260.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 498 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProviderD1Ev(long *param_1)

{
  long lVar1;
  long *plVar2;
  
  if (*param_1 != 0) {
    lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
    if (lVar1 == 0) {
      _ZN8firebase9LogAssertEPKcz("app != nullptr");
    }
    plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
    (**(code **)(*plVar2 + 0xb0))(plVar2,*(undefined8 *)(*param_1 + 8));
    if ((void *)*param_1 != (void *)0x0) {
      _ZdlPv((void *)*param_1);
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
<a id="insn-00bda8fc"></a> `00bda8fc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bda900"></a> `00bda900` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda904"></a> `00bda904` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bda908"></a> `00bda908` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bda90c"></a> `00bda90c` | `88 02 00 b4` | cbz x8,0x00bda95c | `CONDITIONAL_JUMP`
<a id="insn-00bda910"></a> `00bda910` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bda914"></a> `00bda914` | `53 02 02 94` | bl 0x00c5b260 | `UNCONDITIONAL_CALL`
<a id="insn-00bda918"></a> `00bda918` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bda91c"></a> `00bda91c` | `80 00 00 b5` | cbnz x0,0x00bda92c | `CONDITIONAL_JUMP`
<a id="insn-00bda920"></a> `00bda920` | `c0 b6 ff 90` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bda924"></a> `00bda924` | `00 60 17 91` | add x0,x0,#0x5d8 | `FALL_THROUGH`
<a id="insn-00bda928"></a> `00bda928` | `b6 01 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bda92c"></a> `00bda92c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda930"></a> `00bda930` | `d4 01 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bda934"></a> `00bda934` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bda938"></a> `00bda938` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bda93c"></a> `00bda93c` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bda940"></a> `00bda940` | `28 59 40 f9` | ldr x8,[x9, #0xb0] | `FALL_THROUGH`
<a id="insn-00bda944"></a> `00bda944` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda948"></a> `00bda948` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bda94c"></a> `00bda94c` | `80 00 00 b4` | cbz x0,0x00bda95c | `CONDITIONAL_JUMP`
<a id="insn-00bda950"></a> `00bda950` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda954"></a> `00bda954` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bda958"></a> `00bda958` | `56 f5 01 14` | b 0x00c57eb0 | `CALL_TERMINATOR`
<a id="insn-00bda95c"></a> `00bda95c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda960"></a> `00bda960` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bda964"></a> `00bda964` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bda8fc`](#insn-00bda8fc) 範囲 `[['00bda8fc', '00bda90f']]`
  - `CONDITIONAL_JUMP` [`00bda90c`](#insn-00bda90c) → [`00bda95c`](#insn-00bda95c)
  - `FALL_THROUGH` [`00bda90c`](#insn-00bda90c) → [`00bda910`](#insn-00bda910)
- ブロック [`00bda910`](#insn-00bda910) 範囲 `[['00bda910', '00bda91f']]`
  - `CONDITIONAL_JUMP` [`00bda91c`](#insn-00bda91c) → [`00bda92c`](#insn-00bda92c)
  - `FALL_THROUGH` [`00bda91c`](#insn-00bda91c) → [`00bda920`](#insn-00bda920)
- ブロック [`00bda920`](#insn-00bda920) 範囲 `[['00bda920', '00bda92b']]`
  - `FALL_THROUGH` [`00bda928`](#insn-00bda928) → [`00bda92c`](#insn-00bda92c)
- ブロック [`00bda92c`](#insn-00bda92c) 範囲 `[['00bda92c', '00bda94f']]`
  - `CONDITIONAL_JUMP` [`00bda94c`](#insn-00bda94c) → [`00bda95c`](#insn-00bda95c)
  - `FALL_THROUGH` [`00bda94c`](#insn-00bda94c) → [`00bda950`](#insn-00bda950)
- ブロック [`00bda950`](#insn-00bda950) 範囲 `[['00bda950', '00bda95b']]`
- ブロック [`00bda95c`](#insn-00bda95c) 範囲 `[['00bda95c', '00bda967']]`

## 命令位置別の参照

- [`00bda8fc`](#insn-00bda8fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda900`](#insn-00bda900) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda90c`](#insn-00bda90c) → [`00bda95c`](#insn-00bda95c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda914`](#insn-00bda914) → [`00c5b260`](../00c5b/00c5b260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b260` · 推定シンボル `None` · 推定型 `None`
- [`00bda91c`](#insn-00bda91c) → [`00bda92c`](#insn-00bda92c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda924`](#insn-00bda924) → `002b25d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bda928`](#insn-00bda928) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bda930`](#insn-00bda930) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bda94c`](#insn-00bda94c) → [`00bda95c`](#insn-00bda95c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda950`](#insn-00bda950) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda958`](#insn-00bda958) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bda95c`](#insn-00bda95c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bda8fc`](#insn-00bda8fc)

~~~json
{
  "source": "00bda8fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda900`](#insn-00bda900)

~~~json
{
  "source": "00bda900",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda90c`](#insn-00bda90c)

~~~json
{
  "source": "00bda90c",
  "target": "00bda95c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda914`](#insn-00bda914)

~~~json
{
  "source": "00bda914",
  "target": "00c5b260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda91c`](#insn-00bda91c)

~~~json
{
  "source": "00bda91c",
  "target": "00bda92c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda924`](#insn-00bda924)

~~~json
{
  "source": "00bda924",
  "target": "002b25d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b25d8",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b25d8",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bda928`](#insn-00bda928)

~~~json
{
  "source": "00bda928",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda930`](#insn-00bda930)

~~~json
{
  "source": "00bda930",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda94c`](#insn-00bda94c)

~~~json
{
  "source": "00bda94c",
  "target": "00bda95c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda950`](#insn-00bda950)

~~~json
{
  "source": "00bda950",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda958`](#insn-00bda958)

~~~json
{
  "source": "00bda958",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda95c`](#insn-00bda95c)

~~~json
{
  "source": "00bda95c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
