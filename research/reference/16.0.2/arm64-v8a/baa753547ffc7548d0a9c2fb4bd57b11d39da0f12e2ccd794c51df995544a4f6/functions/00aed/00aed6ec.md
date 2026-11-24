# 00aed6ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aed650`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed650.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-b2ee0342e56c878997de4c0c1d4f7c0c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aee6e0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee6e0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-eb2ca4c3a0befcbf128326100674e02a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aed6ec",
  "name": "FUN_00aed6ec",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed064d9b1a69d303eab2df5b686470905769f3f9bb8b5a164f21d6e1c3adc411",
  "source_text_sha256": "ed064d9b1a69d303eab2df5b686470905769f3f9bb8b5a164f21d6e1c3adc411",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aed6ec",
        "00aed797"
      ]
    ],
    "bytes_sha256": "304c87dd333456e18acae17d2b4d1436c3473fd9990e317d1a823ca8d7678ac7",
    "instruction_count": 43,
    "instruction_bytes": 172,
    "body_bytes": 172,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [008b6efc](../008b6/008b6efc.md)
- [00a46944](../00a46/00a46944.md)
- [00a46c0c](../00a46/00a46c0c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1072 bytes

~~~c

void FUN_00aed6ec(long param_1,undefined8 *param_2,int *param_3)

{
  int *piVar1;
  int iVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  iVar2 = *param_3;
  if (iVar2 == 4) {
    lVar5 = *(long *)(param_1 + 8);
    piVar1 = (int *)(lVar5 + 0x846d0);
                    /* try { // try from 00aed74c to 00bed757 has its CatchHandler @ 00aedacc */
    iVar2 = 0;
    if (*piVar1 + 1U < 3) {
      iVar2 = *piVar1 + 1;
    }
    uVar3 = *param_2;
    *(undefined1 *)((long)&fde_table_entry_00335ff0.data_loc + lVar5) = 1;
    *piVar1 = *(int *)(param_1 + (long)iVar2 * 4 + 0x10);
    uVar3 = FUN_008b6efc(uVar3);
    uVar3 = FUN_00a46944(uVar3,0);
    FUN_00a46c0c(uVar3,*piVar1 + 0x86);
    *(undefined1 *)(lVar5 + 0x846d4) = 1;
    return;
  }
  if (iVar2 == 3) {
    uVar3 = FUN_0047ad34();
    uVar4 = 0xb;
  }
  else {
    if (iVar2 != 0) {
      return;
    }
    uVar3 = FUN_0047ad34();
                    /* try { // try from 00aed714 to 00bed71b has its CatchHandler @ 00aedae8 */
    uVar4 = 10;
  }
  FUN_0047ce14(uVar3,uVar4,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aed6ec"></a> `00aed6ec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aed6f0"></a> `00aed6f0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed6f4"></a> `00aed6f4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aed6f8"></a> `00aed6f8` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aed6fc"></a> `00aed6fc` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00aed700"></a> `00aed700` | `a0 01 00 54` | b.eq 0x00aed734 | `CONDITIONAL_JUMP`
<a id="insn-00aed704"></a> `00aed704` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aed708"></a> `00aed708` | `a0 00 00 54` | b.eq 0x00aed71c | `CONDITIONAL_JUMP`
<a id="insn-00aed70c"></a> `00aed70c` | `08 04 00 35` | cbnz w8,0x00aed78c | `CONDITIONAL_JUMP`
<a id="insn-00aed710"></a> `00aed710` | `89 35 e6 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-00aed714"></a> `00aed714` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00aed718"></a> `00aed718` | `03 00 00 14` | b 0x00aed724 | `UNCONDITIONAL_JUMP`
<a id="insn-00aed71c"></a> `00aed71c` | `86 35 e6 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-00aed720"></a> `00aed720` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aed724"></a> `00aed724` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aed728"></a> `00aed728` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed72c"></a> `00aed72c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aed730"></a> `00aed730` | `b9 3d e6 17` | b 0x0047ce14 | `CALL_TERMINATOR`
<a id="insn-00aed734"></a> `00aed734` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aed738"></a> `00aed738` | `34 00 80 52` | mov w20,#0x1 | `FALL_THROUGH`
<a id="insn-00aed73c"></a> `00aed73c` | `09 11 42 91` | add x9,x8,#0x84, LSL #12 | `FALL_THROUGH`
<a id="insn-00aed740"></a> `00aed740` | `33 41 1b 91` | add x19,x9,#0x6d0 | `FALL_THROUGH`
<a id="insn-00aed744"></a> `00aed744` | `69 02 40 b9` | ldr w9,[x19] | `FALL_THROUGH`
<a id="insn-00aed748"></a> `00aed748` | `2a 05 00 11` | add w10,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aed74c"></a> `00aed74c` | `5f 0d 00 71` | cmp w10,#0x3 | `FALL_THROUGH`
<a id="insn-00aed750"></a> `00aed750` | `8a fe 8b 52` | mov w10,#0x5ff4 | `FALL_THROUGH`
<a id="insn-00aed754"></a> `00aed754` | `e9 27 89 1a` | csinc w9,wzr,w9,cs | `FALL_THROUGH`
<a id="insn-00aed758"></a> `00aed758` | `6a 06 a0 72` | movk w10,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aed75c"></a> `00aed75c` | `09 c8 29 8b` | add x9,x0,w9, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00aed760"></a> `00aed760` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-00aed764"></a> `00aed764` | `14 69 2a 38` | strb w20,[x8, x10, LSL ] | `FALL_THROUGH`
<a id="insn-00aed768"></a> `00aed768` | `29 11 40 b9` | ldr w9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00aed76c"></a> `00aed76c` | `69 02 00 b9` | str w9,[x19] | `FALL_THROUGH`
<a id="insn-00aed770"></a> `00aed770` | `e3 25 f7 97` | bl 0x008b6efc | `UNCONDITIONAL_CALL`
<a id="insn-00aed774"></a> `00aed774` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aed778"></a> `00aed778` | `73 64 fd 97` | bl 0x00a46944 | `UNCONDITIONAL_CALL`
<a id="insn-00aed77c"></a> `00aed77c` | `68 02 40 b9` | ldr w8,[x19] | `FALL_THROUGH`
<a id="insn-00aed780"></a> `00aed780` | `01 19 02 11` | add w1,w8,#0x86 | `FALL_THROUGH`
<a id="insn-00aed784"></a> `00aed784` | `22 65 fd 97` | bl 0x00a46c0c | `UNCONDITIONAL_CALL`
<a id="insn-00aed788"></a> `00aed788` | `74 12 00 39` | strb w20,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00aed78c"></a> `00aed78c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed790"></a> `00aed790` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aed794"></a> `00aed794` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aed6ec`](#insn-00aed6ec) 範囲 `[['00aed6ec', '00aed703']]`
  - `CONDITIONAL_JUMP` [`00aed700`](#insn-00aed700) → [`00aed734`](#insn-00aed734)
  - `FALL_THROUGH` [`00aed700`](#insn-00aed700) → [`00aed704`](#insn-00aed704)
- ブロック [`00aed704`](#insn-00aed704) 範囲 `[['00aed704', '00aed70b']]`
  - `CONDITIONAL_JUMP` [`00aed708`](#insn-00aed708) → [`00aed71c`](#insn-00aed71c)
  - `FALL_THROUGH` [`00aed708`](#insn-00aed708) → [`00aed70c`](#insn-00aed70c)
- ブロック [`00aed70c`](#insn-00aed70c) 範囲 `[['00aed70c', '00aed70f']]`
  - `CONDITIONAL_JUMP` [`00aed70c`](#insn-00aed70c) → [`00aed78c`](#insn-00aed78c)
  - `FALL_THROUGH` [`00aed70c`](#insn-00aed70c) → [`00aed710`](#insn-00aed710)
- ブロック [`00aed710`](#insn-00aed710) 範囲 `[['00aed710', '00aed713']]`
  - `FALL_THROUGH` [`00aed710`](#insn-00aed710) → [`00aed714`](#insn-00aed714)
- ブロック [`00aed714`](#insn-00aed714) 範囲 `[['00aed714', '00aed71b']]`
  - `UNCONDITIONAL_JUMP` [`00aed718`](#insn-00aed718) → [`00aed724`](#insn-00aed724)
- ブロック [`00aed71c`](#insn-00aed71c) 範囲 `[['00aed71c', '00aed723']]`
  - `FALL_THROUGH` [`00aed720`](#insn-00aed720) → [`00aed724`](#insn-00aed724)
- ブロック [`00aed724`](#insn-00aed724) 範囲 `[['00aed724', '00aed733']]`
- ブロック [`00aed734`](#insn-00aed734) 範囲 `[['00aed734', '00aed74b']]`
  - `FALL_THROUGH` [`00aed748`](#insn-00aed748) → [`00aed74c`](#insn-00aed74c)
- ブロック [`00aed74c`](#insn-00aed74c) 範囲 `[['00aed74c', '00aed78b']]`
  - `FALL_THROUGH` [`00aed788`](#insn-00aed788) → [`00aed78c`](#insn-00aed78c)
- ブロック [`00aed78c`](#insn-00aed78c) 範囲 `[['00aed78c', '00aed797']]`

## 命令位置別の参照

- [`00aed6ec`](#insn-00aed6ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed6f0`](#insn-00aed6f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed700`](#insn-00aed700) → [`00aed734`](#insn-00aed734) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed708`](#insn-00aed708) → [`00aed71c`](#insn-00aed71c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed70c`](#insn-00aed70c) → [`00aed78c`](#insn-00aed78c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed710`](#insn-00aed710) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`00aed718`](#insn-00aed718) → [`00aed724`](#insn-00aed724) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed71c`](#insn-00aed71c) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`00aed728`](#insn-00aed728) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed72c`](#insn-00aed72c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed730`](#insn-00aed730) → [`0047ce14`](../0047c/0047ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ce14` · 推定シンボル `None` · 推定型 `None`
- [`00aed764`](#insn-00aed764) → `00335ff4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aed770`](#insn-00aed770) → [`008b6efc`](../008b6/008b6efc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6efc` · 推定シンボル `None` · 推定型 `None`
- [`00aed778`](#insn-00aed778) → [`00a46944`](../00a46/00a46944.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a46944` · 推定シンボル `None` · 推定型 `None`
- [`00aed784`](#insn-00aed784) → [`00a46c0c`](../00a46/00a46c0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a46c0c` · 推定シンボル `None` · 推定型 `None`
- [`00aed78c`](#insn-00aed78c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed790`](#insn-00aed790) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aed6ec`](#insn-00aed6ec)

~~~json
{
  "source": "00aed6ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed6f0`](#insn-00aed6f0)

~~~json
{
  "source": "00aed6f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed700`](#insn-00aed700)

~~~json
{
  "source": "00aed700",
  "target": "00aed734",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed708`](#insn-00aed708)

~~~json
{
  "source": "00aed708",
  "target": "00aed71c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed70c`](#insn-00aed70c)

~~~json
{
  "source": "00aed70c",
  "target": "00aed78c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed710`](#insn-00aed710)

~~~json
{
  "source": "00aed710",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed718`](#insn-00aed718)

~~~json
{
  "source": "00aed718",
  "target": "00aed724",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed71c`](#insn-00aed71c)

~~~json
{
  "source": "00aed71c",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed728`](#insn-00aed728)

~~~json
{
  "source": "00aed728",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed72c`](#insn-00aed72c)

~~~json
{
  "source": "00aed72c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed730`](#insn-00aed730)

~~~json
{
  "source": "00aed730",
  "target": "0047ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed764`](#insn-00aed764)

~~~json
{
  "source": "00aed764",
  "target": "00335ff4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335ff0",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "2481750000000a00",
  "capture_start": "00335ff0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aed770`](#insn-00aed770)

~~~json
{
  "source": "00aed770",
  "target": "008b6efc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed778`](#insn-00aed778)

~~~json
{
  "source": "00aed778",
  "target": "00a46944",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed784`](#insn-00aed784)

~~~json
{
  "source": "00aed784",
  "target": "00a46c0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed78c`](#insn-00aed78c)

~~~json
{
  "source": "00aed78c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed790`](#insn-00aed790)

~~~json
{
  "source": "00aed790",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
