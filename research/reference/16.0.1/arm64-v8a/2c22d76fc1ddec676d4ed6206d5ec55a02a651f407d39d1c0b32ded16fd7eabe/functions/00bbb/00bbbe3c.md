# 00bbbe3c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbba14`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbba14.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-ced8486a7f651c88f75d667d155d1de9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbbed8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbed8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-7ccb268ef4c03666833291ce30fc360a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbe3c",
  "name": "_ZN8firebase9messaging21UnsubscribeLastResultEv",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "87daaf807fdddbcc60985dd66832c952c56f356658d000230030251a482c6b8d",
  "source_text_sha256": "87daaf807fdddbcc60985dd66832c952c56f356658d000230030251a482c6b8d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbe3c",
        "00bbbee3"
      ]
    ],
    "bytes_sha256": "45f335e17383d94d68e78eabbfe5621e408737a1885959d8f2ad72d6595605d3",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5abe0](../00c5a/00c5abe0.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5ad50](../00c5a/00c5ad50.md)
- [00c5ae10](../00c5a/00c5ae10.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5d270](../00c5d/00c5d270.md)

## 関連文字列（未確認候補）

~~~text
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 879 bytes

~~~c

void _ZN8firebase9messaging21UnsubscribeLastResultEv(long param_1)

{
  long lVar1;
  long lVar2;
  
  if (DAT_01126360 == 0) {
    _ZN8firebase9LogAssertEPKcz("internal::IsInitialized()");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar1 = _ZN8firebase9messaging10FutureData3GetEv();
                    /* try { // try from 00bbbe6c to 00cbbefb has its CatchHandler @ 00bbb92c */
    _ZN8firebase5Mutex7AcquireEv(lVar1 + 8);
    lVar2 = *(long *)(lVar1 + 0x50);
    _ZN8firebase5Mutex7ReleaseEv(lVar1 + 8);
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
    _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0x80);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbe3c"></a> `00bbbe3c` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbbe40"></a> `00bbbe40` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbe44"></a> `00bbbe44` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbe48"></a> `00bbbe48` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbbe4c"></a> `00bbbe4c` | `49 2b 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbe50"></a> `00bbbe50` | `29 b1 41 f9` | ldr x9,[x9, #0x360] | `FALL_THROUGH`
<a id="insn-00bbbe54"></a> `00bbbe54` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bbbe58"></a> `00bbbe58` | `89 02 00 b4` | cbz x9,0x00bbbea8 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe5c"></a> `00bbbe5c` | `05 85 02 94` | bl 0x00c5d270 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe60"></a> `00bbbe60` | `15 20 00 91` | add x21,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bbbe64"></a> `00bbbe64` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbbe68"></a> `00bbbe68` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbbe6c"></a> `00bbbe6c` | `e5 7a 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe70"></a> `00bbbe70` | `96 2a 40 f9` | ldr x22,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00bbbe74"></a> `00bbbe74` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbbe78"></a> `00bbbe78` | `e6 7a 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe7c"></a> `00bbbe7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbe80"></a> `00bbbe80` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbbe84"></a> `00bbbe84` | `7b 7b 02 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe88"></a> `00bbbe88` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bbbe8c"></a> `00bbbe8c` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbe90"></a> `00bbbe90` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbbe94"></a> `00bbbe94` | `df 7b 02 94` | bl 0x00c5ae10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe98"></a> `00bbbe98` | `c1 02 02 91` | add x1,x22,#0x80 | `FALL_THROUGH`
<a id="insn-00bbbe9c"></a> `00bbbe9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbea0"></a> `00bbbea0` | `ac 7b 02 94` | bl 0x00c5ad50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbea4"></a> `00bbbea4` | `0c 00 00 14` | b 0x00bbbed4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbea8"></a> `00bbbea8` | `20 b7 ff f0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbbeac"></a> `00bbbeac` | `00 54 24 91` | add x0,x0,#0x915 | `FALL_THROUGH`
<a id="insn-00bbbeb0"></a> `00bbbeb0` | `54 7c 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbeb4"></a> `00bbbeb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbeb8"></a> `00bbbeb8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbbebc"></a> `00bbbebc` | `6d 7b 02 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbec0"></a> `00bbbec0` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bbbec4"></a> `00bbbec4` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbec8"></a> `00bbbec8` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbbecc"></a> `00bbbecc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbbed0"></a> `00bbbed0` | `44 7b 02 94` | bl 0x00c5abe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbed4"></a> `00bbbed4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbed8"></a> `00bbbed8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbedc"></a> `00bbbedc` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbbee0"></a> `00bbbee0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbbe3c`](#insn-00bbbe3c) 範囲 `[['00bbbe3c', '00bbbe5b']]`
  - `CONDITIONAL_JUMP` [`00bbbe58`](#insn-00bbbe58) → [`00bbbea8`](#insn-00bbbea8)
  - `FALL_THROUGH` [`00bbbe58`](#insn-00bbbe58) → [`00bbbe5c`](#insn-00bbbe5c)
- ブロック [`00bbbe5c`](#insn-00bbbe5c) 範囲 `[['00bbbe5c', '00bbbe6b']]`
  - `FALL_THROUGH` [`00bbbe68`](#insn-00bbbe68) → [`00bbbe6c`](#insn-00bbbe6c)
- ブロック [`00bbbe6c`](#insn-00bbbe6c) 範囲 `[['00bbbe6c', '00bbbea7']]`
  - `UNCONDITIONAL_JUMP` [`00bbbea4`](#insn-00bbbea4) → [`00bbbed4`](#insn-00bbbed4)
- ブロック [`00bbbea8`](#insn-00bbbea8) 範囲 `[['00bbbea8', '00bbbed3']]`
  - `FALL_THROUGH` [`00bbbed0`](#insn-00bbbed0) → [`00bbbed4`](#insn-00bbbed4)
- ブロック [`00bbbed4`](#insn-00bbbed4) 範囲 `[['00bbbed4', '00bbbee3']]`

## 命令位置別の参照

- [`00bbbe3c`](#insn-00bbbe3c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe40`](#insn-00bbbe40) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe44`](#insn-00bbbe44) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe50`](#insn-00bbbe50) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbe58`](#insn-00bbbe58) → [`00bbbea8`](#insn-00bbbea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe5c`](#insn-00bbbe5c) → [`00c5d270`](../00c5d/00c5d270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d270` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe6c`](#insn-00bbbe6c) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe78`](#insn-00bbbe78) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe84`](#insn-00bbbe84) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe94`](#insn-00bbbe94) → [`00c5ae10`](../00c5a/00c5ae10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae10` · 推定シンボル `None` · 推定型 `None`
- [`00bbbea0`](#insn-00bbbea0) → [`00c5ad50`](../00c5a/00c5ad50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad50` · 推定シンボル `None` · 推定型 `None`
- [`00bbbea4`](#insn-00bbbea4) → [`00bbbed4`](#insn-00bbbed4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbeac`](#insn-00bbbeac) → `002a2915`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbeb0`](#insn-00bbbeb0) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bbbebc`](#insn-00bbbebc) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bbbed0`](#insn-00bbbed0) → [`00c5abe0`](../00c5a/00c5abe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5abe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbed4`](#insn-00bbbed4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbed8`](#insn-00bbbed8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbe3c`](#insn-00bbbe3c)

~~~json
{
  "source": "00bbbe3c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe40`](#insn-00bbbe40)

~~~json
{
  "source": "00bbbe40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe44`](#insn-00bbbe44)

~~~json
{
  "source": "00bbbe44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe50`](#insn-00bbbe50)

~~~json
{
  "source": "00bbbe50",
  "target": "01126360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126360",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbe58`](#insn-00bbbe58)

~~~json
{
  "source": "00bbbe58",
  "target": "00bbbea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe5c`](#insn-00bbbe5c)

~~~json
{
  "source": "00bbbe5c",
  "target": "00c5d270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe6c`](#insn-00bbbe6c)

~~~json
{
  "source": "00bbbe6c",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe78`](#insn-00bbbe78)

~~~json
{
  "source": "00bbbe78",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe84`](#insn-00bbbe84)

~~~json
{
  "source": "00bbbe84",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe94`](#insn-00bbbe94)

~~~json
{
  "source": "00bbbe94",
  "target": "00c5ae10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbea0`](#insn-00bbbea0)

~~~json
{
  "source": "00bbbea0",
  "target": "00c5ad50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbea4`](#insn-00bbbea4)

~~~json
{
  "source": "00bbbea4",
  "target": "00bbbed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbeac`](#insn-00bbbeac)

~~~json
{
  "source": "00bbbeac",
  "target": "002a2915",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2915",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2915",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbbeb0`](#insn-00bbbeb0)

~~~json
{
  "source": "00bbbeb0",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbebc`](#insn-00bbbebc)

~~~json
{
  "source": "00bbbebc",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbed0`](#insn-00bbbed0)

~~~json
{
  "source": "00bbbed0",
  "target": "00c5abe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbed4`](#insn-00bbbed4)

~~~json
{
  "source": "00bbbed4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbed8`](#insn-00bbbed8)

~~~json
{
  "source": "00bbbed8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
