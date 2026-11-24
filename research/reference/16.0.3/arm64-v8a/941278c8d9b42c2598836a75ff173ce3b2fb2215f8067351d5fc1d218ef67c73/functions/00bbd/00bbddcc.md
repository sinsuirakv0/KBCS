# 00bbddcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbcdd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcdd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-8e8fcbad6a66f2bcc6e8e5ee7111a91d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbddcc",
  "name": "_ZN8firebase9messaging18GetTokenLastResultEv",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f05bdb9e256ee752a4e3a3f0e60d003d41554f93e58368a52887902f9653bbf",
  "source_text_sha256": "0f05bdb9e256ee752a4e3a3f0e60d003d41554f93e58368a52887902f9653bbf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbddcc",
        "00bbde73"
      ]
    ],
    "bytes_sha256": "af40789d275bca8ff1e28383d3334794ca6c1c9aee86a370823c6501242c6578",
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

- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5bc80](../00c5b/00c5bc80.md)
- [00c5bd10](../00c5b/00c5bd10.md)
- [00c5bdf0](../00c5b/00c5bdf0.md)
- [00c5beb0](../00c5b/00c5beb0.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5e310](../00c5e/00c5e310.md)

## 関連文字列（未確認候補）

~~~text
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1167 bytes

~~~c

void _ZN8firebase9messaging18GetTokenLastResultEv(long param_1)

{
  long lVar1;
  long lVar2;
  
  if (DAT_01127420 == 0) {
                    /* try { // try from 00bbde40 to 00cbde47 has its CatchHandler @ 00bbded4 */
    _ZN8firebase9LogAssertEPKcz("internal::IsInitialized()");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
                    /* try { // try from 00bbde5c to 00cbde7b has its CatchHandler @ 00bbdee0 */
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar1 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase5Mutex7AcquireEv(lVar1 + 8);
    lVar2 = *(long *)(lVar1 + 0x50);
    _ZN8firebase5Mutex7ReleaseEv(lVar1 + 8);
                    /* try { // try from 00bbde0c to 00cbde13 has its CatchHandler @ 00bbdee0 */
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
                    /* try { // try from 00bbde28 to 00cbde2f has its CatchHandler @ 00bbded8 */
    _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0xc0);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbddcc"></a> `00bbddcc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbddd0"></a> `00bbddd0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbddd4"></a> `00bbddd4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbddd8"></a> `00bbddd8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbdddc"></a> `00bbdddc` | `49 2b 00 d0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbdde0"></a> `00bbdde0` | `29 11 42 f9` | ldr x9,[x9, #0x420] | `FALL_THROUGH`
<a id="insn-00bbdde4"></a> `00bbdde4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bbdde8"></a> `00bbdde8` | `89 02 00 b4` | cbz x9,0x00bbde38 | `CONDITIONAL_JUMP`
<a id="insn-00bbddec"></a> `00bbddec` | `49 81 02 94` | bl 0x00c5e310 | `UNCONDITIONAL_CALL`
<a id="insn-00bbddf0"></a> `00bbddf0` | `15 20 00 91` | add x21,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bbddf4"></a> `00bbddf4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbddf8"></a> `00bbddf8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbddfc"></a> `00bbddfc` | `29 77 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde00"></a> `00bbde00` | `96 2a 40 f9` | ldr x22,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00bbde04"></a> `00bbde04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbde08"></a> `00bbde08` | `2a 77 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde0c"></a> `00bbde0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbde10"></a> `00bbde10` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbde14"></a> `00bbde14` | `bf 77 02 94` | bl 0x00c5bd10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde18"></a> `00bbde18` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bbde1c"></a> `00bbde1c` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbde20"></a> `00bbde20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbde24"></a> `00bbde24` | `23 78 02 94` | bl 0x00c5beb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde28"></a> `00bbde28` | `c1 02 03 91` | add x1,x22,#0xc0 | `FALL_THROUGH`
<a id="insn-00bbde2c"></a> `00bbde2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbde30"></a> `00bbde30` | `f0 77 02 94` | bl 0x00c5bdf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde34"></a> `00bbde34` | `0c 00 00 14` | b 0x00bbde64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbde38"></a> `00bbde38` | `20 b7 ff b0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbde3c"></a> `00bbde3c` | `00 4c 26 91` | add x0,x0,#0x993 | `FALL_THROUGH`
<a id="insn-00bbde40"></a> `00bbde40` | `98 78 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde44"></a> `00bbde44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbde48"></a> `00bbde48` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbde4c"></a> `00bbde4c` | `b1 77 02 94` | bl 0x00c5bd10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde50"></a> `00bbde50` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bbde54"></a> `00bbde54` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbde58"></a> `00bbde58` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbde5c"></a> `00bbde5c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbde60"></a> `00bbde60` | `88 77 02 94` | bl 0x00c5bc80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde64"></a> `00bbde64` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbde68"></a> `00bbde68` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbde6c"></a> `00bbde6c` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbde70"></a> `00bbde70` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbddcc`](#insn-00bbddcc) 範囲 `[['00bbddcc', '00bbddeb']]`
  - `CONDITIONAL_JUMP` [`00bbdde8`](#insn-00bbdde8) → [`00bbde38`](#insn-00bbde38)
  - `FALL_THROUGH` [`00bbdde8`](#insn-00bbdde8) → [`00bbddec`](#insn-00bbddec)
- ブロック [`00bbddec`](#insn-00bbddec) 範囲 `[['00bbddec', '00bbde0b']]`
  - `FALL_THROUGH` [`00bbde08`](#insn-00bbde08) → [`00bbde0c`](#insn-00bbde0c)
- ブロック [`00bbde0c`](#insn-00bbde0c) 範囲 `[['00bbde0c', '00bbde27']]`
  - `FALL_THROUGH` [`00bbde24`](#insn-00bbde24) → [`00bbde28`](#insn-00bbde28)
- ブロック [`00bbde28`](#insn-00bbde28) 範囲 `[['00bbde28', '00bbde37']]`
  - `UNCONDITIONAL_JUMP` [`00bbde34`](#insn-00bbde34) → [`00bbde64`](#insn-00bbde64)
- ブロック [`00bbde38`](#insn-00bbde38) 範囲 `[['00bbde38', '00bbde3f']]`
  - `FALL_THROUGH` [`00bbde3c`](#insn-00bbde3c) → [`00bbde40`](#insn-00bbde40)
- ブロック [`00bbde40`](#insn-00bbde40) 範囲 `[['00bbde40', '00bbde5b']]`
  - `FALL_THROUGH` [`00bbde58`](#insn-00bbde58) → [`00bbde5c`](#insn-00bbde5c)
- ブロック [`00bbde5c`](#insn-00bbde5c) 範囲 `[['00bbde5c', '00bbde63']]`
  - `FALL_THROUGH` [`00bbde60`](#insn-00bbde60) → [`00bbde64`](#insn-00bbde64)
- ブロック [`00bbde64`](#insn-00bbde64) 範囲 `[['00bbde64', '00bbde73']]`

## 命令位置別の参照

- [`00bbddcc`](#insn-00bbddcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddd0`](#insn-00bbddd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddd4`](#insn-00bbddd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdde0`](#insn-00bbdde0) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbdde8`](#insn-00bbdde8) → [`00bbde38`](#insn-00bbde38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddec`](#insn-00bbddec) → [`00c5e310`](../00c5e/00c5e310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e310` · 推定シンボル `None` · 推定型 `None`
- [`00bbddfc`](#insn-00bbddfc) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bbde08`](#insn-00bbde08) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bbde14`](#insn-00bbde14) → [`00c5bd10`](../00c5b/00c5bd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd10` · 推定シンボル `None` · 推定型 `None`
- [`00bbde24`](#insn-00bbde24) → [`00c5beb0`](../00c5b/00c5beb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5beb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbde30`](#insn-00bbde30) → [`00c5bdf0`](../00c5b/00c5bdf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bdf0` · 推定シンボル `None` · 推定型 `None`
- [`00bbde34`](#insn-00bbde34) → [`00bbde64`](#insn-00bbde64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde3c`](#insn-00bbde3c) → `002a2993`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbde40`](#insn-00bbde40) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbde4c`](#insn-00bbde4c) → [`00c5bd10`](../00c5b/00c5bd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd10` · 推定シンボル `None` · 推定型 `None`
- [`00bbde60`](#insn-00bbde60) → [`00c5bc80`](../00c5b/00c5bc80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc80` · 推定シンボル `None` · 推定型 `None`
- [`00bbde64`](#insn-00bbde64) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde68`](#insn-00bbde68) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbddcc`](#insn-00bbddcc)

~~~json
{
  "source": "00bbddcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddd0`](#insn-00bbddd0)

~~~json
{
  "source": "00bbddd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddd4`](#insn-00bbddd4)

~~~json
{
  "source": "00bbddd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdde0`](#insn-00bbdde0)

~~~json
{
  "source": "00bbdde0",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbdde8`](#insn-00bbdde8)

~~~json
{
  "source": "00bbdde8",
  "target": "00bbde38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddec`](#insn-00bbddec)

~~~json
{
  "source": "00bbddec",
  "target": "00c5e310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbddfc`](#insn-00bbddfc)

~~~json
{
  "source": "00bbddfc",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde08`](#insn-00bbde08)

~~~json
{
  "source": "00bbde08",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde14`](#insn-00bbde14)

~~~json
{
  "source": "00bbde14",
  "target": "00c5bd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde24`](#insn-00bbde24)

~~~json
{
  "source": "00bbde24",
  "target": "00c5beb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde30`](#insn-00bbde30)

~~~json
{
  "source": "00bbde30",
  "target": "00c5bdf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde34`](#insn-00bbde34)

~~~json
{
  "source": "00bbde34",
  "target": "00bbde64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde3c`](#insn-00bbde3c)

~~~json
{
  "source": "00bbde3c",
  "target": "002a2993",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2993",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2993",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbde40`](#insn-00bbde40)

~~~json
{
  "source": "00bbde40",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde4c`](#insn-00bbde4c)

~~~json
{
  "source": "00bbde4c",
  "target": "00c5bd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde60`](#insn-00bbde60)

~~~json
{
  "source": "00bbde60",
  "target": "00c5bc80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde64`](#insn-00bbde64)

~~~json
{
  "source": "00bbde64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde68`](#insn-00bbde68)

~~~json
{
  "source": "00bbde68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
