# 00bcdab4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcd68c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd68c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-12326505fba73c50a54de551d678ead8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcdb50`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdb50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-83bac921495bdd1ddc9d4115688ece24)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdab4",
  "name": "_ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "53eee70fa6c0ae2701d736741fcaba50795995a1d4121d185a4452435724ba40",
  "source_text_sha256": "53eee70fa6c0ae2701d736741fcaba50795995a1d4121d185a4452435724ba40",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdab4",
        "00bcdb43"
      ]
    ],
    "bytes_sha256": "ff126cbf92e8a14989fd2ee9c0be3eb4706096310419759a20b097f914d1e606",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5d990](../00c5d/00c5d990.md)

## 呼び出し先

- [00c5aba0](../00c5a/00c5aba0.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5bef0](../00c5b/00c5bef0.md)
- [00c5da80](../00c5d/00c5da80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1057 bytes

~~~c

void _ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE(undefined8 *param_1)

{
  long *plVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_1);
                    /* try { // try from 00bcdad4 to 00ccdadb has its CatchHandler @ 00bcea50 */
  _ZN8firebase4auth4Auth3appEv(param_1);
  uVar2 = _ZNK8firebase3App14GetPlatformAppEv();
  uVar3 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                    (plVar1,DAT_01126728,DAT_01126738,uVar2);
                    /* try { // try from 00bcdb04 to 00ccdb17 has its CatchHandler @ 00bcea30 */
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar1);
                    /* try { // try from 00bcdb18 to 00ccdb1f has its CatchHandler @ 00bcea40 */
  (**(code **)(*plVar1 + 0xb8))(plVar1,uVar3);
                    /* WARNING: Could not recover jumptable at 0x00bcdb40. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + 0xb8))(plVar1,uVar2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcdab4"></a> `00bcdab4` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcdab8"></a> `00bcdab8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdabc"></a> `00bcdabc` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdac0"></a> `00bcdac0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcdac4"></a> `00bcdac4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcdac8"></a> `00bcdac8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcdacc"></a> `00bcdacc` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcdad0"></a> `00bcdad0` | `6c 35 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdad4"></a> `00bcdad4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcdad8"></a> `00bcdad8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdadc"></a> `00bcdadc` | `e9 3f 02 94` | bl 0x00c5da80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdae0"></a> `00bcdae0` | `04 39 02 94` | bl 0x00c5bef0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdae4"></a> `00bcdae4` | `c8 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcdae8"></a> `00bcdae8` | `c9 2a 00 b0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcdaec"></a> `00bcdaec` | `01 95 43 f9` | ldr x1,[x8, #0x728] | `FALL_THROUGH`
<a id="insn-00bcdaf0"></a> `00bcdaf0` | `22 9d 43 f9` | ldr x2,[x9, #0x738] | `FALL_THROUGH`
<a id="insn-00bcdaf4"></a> `00bcdaf4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcdaf8"></a> `00bcdaf8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdafc"></a> `00bcdafc` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bcdb00"></a> `00bcdb00` | `28 34 02 94` | bl 0x00c5aba0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdb04"></a> `00bcdb04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcdb08"></a> `00bcdb08` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdb0c"></a> `00bcdb0c` | `15 35 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdb10"></a> `00bcdb10` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcdb14"></a> `00bcdb14` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdb18"></a> `00bcdb18` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcdb1c"></a> `00bcdb1c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcdb20"></a> `00bcdb20` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdb24"></a> `00bcdb24` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcdb28"></a> `00bcdb28` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdb2c"></a> `00bcdb2c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcdb30"></a> `00bcdb30` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdb34"></a> `00bcdb34` | `02 5d 40 f9` | ldr x2,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcdb38"></a> `00bcdb38` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdb3c"></a> `00bcdb3c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcdb40"></a> `00bcdb40` | `40 00 1f d6` | br x2 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bcdab4`](#insn-00bcdab4) 範囲 `[['00bcdab4', '00bcdad3']]`
  - `FALL_THROUGH` [`00bcdad0`](#insn-00bcdad0) → [`00bcdad4`](#insn-00bcdad4)
- ブロック [`00bcdad4`](#insn-00bcdad4) 範囲 `[['00bcdad4', '00bcdb03']]`
  - `FALL_THROUGH` [`00bcdb00`](#insn-00bcdb00) → [`00bcdb04`](#insn-00bcdb04)
- ブロック [`00bcdb04`](#insn-00bcdb04) 範囲 `[['00bcdb04', '00bcdb17']]`
  - `FALL_THROUGH` [`00bcdb14`](#insn-00bcdb14) → [`00bcdb18`](#insn-00bcdb18)
- ブロック [`00bcdb18`](#insn-00bcdb18) 範囲 `[['00bcdb18', '00bcdb43']]`

## 命令位置別の参照

- [`00bcdab4`](#insn-00bcdab4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdab8`](#insn-00bcdab8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdabc`](#insn-00bcdabc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdad0`](#insn-00bcdad0) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bcdadc`](#insn-00bcdadc) → [`00c5da80`](../00c5d/00c5da80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5da80` · 推定シンボル `None` · 推定型 `None`
- [`00bcdae0`](#insn-00bcdae0) → [`00c5bef0`](../00c5b/00c5bef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bef0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdaec`](#insn-00bcdaec) → `01126728`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdaf0`](#insn-00bcdaf0) → `01126738`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdb00`](#insn-00bcdb00) → [`00c5aba0`](../00c5a/00c5aba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aba0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb0c`](#insn-00bcdb0c) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb30`](#insn-00bcdb30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb38`](#insn-00bcdb38) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdab4`](#insn-00bcdab4)

~~~json
{
  "source": "00bcdab4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdab8`](#insn-00bcdab8)

~~~json
{
  "source": "00bcdab8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdabc`](#insn-00bcdabc)

~~~json
{
  "source": "00bcdabc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdad0`](#insn-00bcdad0)

~~~json
{
  "source": "00bcdad0",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdadc`](#insn-00bcdadc)

~~~json
{
  "source": "00bcdadc",
  "target": "00c5da80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdae0`](#insn-00bcdae0)

~~~json
{
  "source": "00bcdae0",
  "target": "00c5bef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdaec`](#insn-00bcdaec)

~~~json
{
  "source": "00bcdaec",
  "target": "01126728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126728",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdaf0`](#insn-00bcdaf0)

~~~json
{
  "source": "00bcdaf0",
  "target": "01126738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126738",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdb00`](#insn-00bcdb00)

~~~json
{
  "source": "00bcdb00",
  "target": "00c5aba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdb0c`](#insn-00bcdb0c)

~~~json
{
  "source": "00bcdb0c",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdb30`](#insn-00bcdb30)

~~~json
{
  "source": "00bcdb30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb38`](#insn-00bcdb38)

~~~json
{
  "source": "00bcdb38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
