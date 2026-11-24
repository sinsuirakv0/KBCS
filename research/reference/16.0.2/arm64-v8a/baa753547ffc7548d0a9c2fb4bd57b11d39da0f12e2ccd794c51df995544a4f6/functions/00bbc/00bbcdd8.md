# 00bbcdd8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbcd3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcd3c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-3d1a90df260122044b5f3a7087af8a26)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbddcc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbddcc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-8e8fcbad6a66f2bcc6e8e5ee7111a91d)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcdd8",
  "name": "_ZN8firebase9messaging18GetTokenLastResultEv",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "830ca9807bb9bb77d453e7800f0488170a1d2ee71a07b0093e9b48ace8ffe6c8",
  "source_text_sha256": "830ca9807bb9bb77d453e7800f0488170a1d2ee71a07b0093e9b48ace8ffe6c8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbcdd8",
        "00bbce7f"
      ]
    ],
    "bytes_sha256": "9b755334d78d100dd652d682a23f0bfa3684b6b25263495d2b056198d6ef5f63",
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

- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5ae20](../00c5a/00c5ae20.md)
- [00c5aee0](../00c5a/00c5aee0.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5d340](../00c5d/00c5d340.md)

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
  
  if (DAT_01126460 == 0) {
                    /* try { // try from 00bbce4c to 00cbce53 has its CatchHandler @ 00bbcee0 */
    _ZN8firebase9LogAssertEPKcz("internal::IsInitialized()");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
                    /* try { // try from 00bbce68 to 00cbce87 has its CatchHandler @ 00bbceec */
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar1 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase5Mutex7AcquireEv(lVar1 + 8);
    lVar2 = *(long *)(lVar1 + 0x50);
    _ZN8firebase5Mutex7ReleaseEv(lVar1 + 8);
                    /* try { // try from 00bbce18 to 00cbce1f has its CatchHandler @ 00bbceec */
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
                    /* try { // try from 00bbce34 to 00cbce3b has its CatchHandler @ 00bbcee4 */
    _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0xc0);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbcdd8"></a> `00bbcdd8` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbcddc"></a> `00bbcddc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcde0"></a> `00bbcde0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcde4"></a> `00bbcde4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbcde8"></a> `00bbcde8` | `49 2b 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbcdec"></a> `00bbcdec` | `29 31 42 f9` | ldr x9,[x9, #0x460] | `FALL_THROUGH`
<a id="insn-00bbcdf0"></a> `00bbcdf0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bbcdf4"></a> `00bbcdf4` | `89 02 00 b4` | cbz x9,0x00bbce44 | `CONDITIONAL_JUMP`
<a id="insn-00bbcdf8"></a> `00bbcdf8` | `52 81 02 94` | bl 0x00c5d340 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcdfc"></a> `00bbcdfc` | `15 20 00 91` | add x21,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bbce00"></a> `00bbce00` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbce04"></a> `00bbce04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbce08"></a> `00bbce08` | `32 77 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce0c"></a> `00bbce0c` | `96 2a 40 f9` | ldr x22,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00bbce10"></a> `00bbce10` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbce14"></a> `00bbce14` | `33 77 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce18"></a> `00bbce18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbce1c"></a> `00bbce1c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbce20"></a> `00bbce20` | `c8 77 02 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce24"></a> `00bbce24` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bbce28"></a> `00bbce28` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbce2c"></a> `00bbce2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbce30"></a> `00bbce30` | `2c 78 02 94` | bl 0x00c5aee0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce34"></a> `00bbce34` | `c1 02 03 91` | add x1,x22,#0xc0 | `FALL_THROUGH`
<a id="insn-00bbce38"></a> `00bbce38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbce3c"></a> `00bbce3c` | `f9 77 02 94` | bl 0x00c5ae20 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce40"></a> `00bbce40` | `0c 00 00 14` | b 0x00bbce70 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbce44"></a> `00bbce44` | `20 b7 ff d0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbce48"></a> `00bbce48` | `00 20 23 91` | add x0,x0,#0x8c8 | `FALL_THROUGH`
<a id="insn-00bbce4c"></a> `00bbce4c` | `a1 78 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce50"></a> `00bbce50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbce54"></a> `00bbce54` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbce58"></a> `00bbce58` | `ba 77 02 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce5c"></a> `00bbce5c` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bbce60"></a> `00bbce60` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbce64"></a> `00bbce64` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbce68"></a> `00bbce68` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbce6c"></a> `00bbce6c` | `91 77 02 94` | bl 0x00c5acb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce70"></a> `00bbce70` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbce74"></a> `00bbce74` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbce78"></a> `00bbce78` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbce7c"></a> `00bbce7c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbcdd8`](#insn-00bbcdd8) 範囲 `[['00bbcdd8', '00bbcdf7']]`
  - `CONDITIONAL_JUMP` [`00bbcdf4`](#insn-00bbcdf4) → [`00bbce44`](#insn-00bbce44)
  - `FALL_THROUGH` [`00bbcdf4`](#insn-00bbcdf4) → [`00bbcdf8`](#insn-00bbcdf8)
- ブロック [`00bbcdf8`](#insn-00bbcdf8) 範囲 `[['00bbcdf8', '00bbce17']]`
  - `FALL_THROUGH` [`00bbce14`](#insn-00bbce14) → [`00bbce18`](#insn-00bbce18)
- ブロック [`00bbce18`](#insn-00bbce18) 範囲 `[['00bbce18', '00bbce33']]`
  - `FALL_THROUGH` [`00bbce30`](#insn-00bbce30) → [`00bbce34`](#insn-00bbce34)
- ブロック [`00bbce34`](#insn-00bbce34) 範囲 `[['00bbce34', '00bbce43']]`
  - `UNCONDITIONAL_JUMP` [`00bbce40`](#insn-00bbce40) → [`00bbce70`](#insn-00bbce70)
- ブロック [`00bbce44`](#insn-00bbce44) 範囲 `[['00bbce44', '00bbce4b']]`
  - `FALL_THROUGH` [`00bbce48`](#insn-00bbce48) → [`00bbce4c`](#insn-00bbce4c)
- ブロック [`00bbce4c`](#insn-00bbce4c) 範囲 `[['00bbce4c', '00bbce67']]`
  - `FALL_THROUGH` [`00bbce64`](#insn-00bbce64) → [`00bbce68`](#insn-00bbce68)
- ブロック [`00bbce68`](#insn-00bbce68) 範囲 `[['00bbce68', '00bbce6f']]`
  - `FALL_THROUGH` [`00bbce6c`](#insn-00bbce6c) → [`00bbce70`](#insn-00bbce70)
- ブロック [`00bbce70`](#insn-00bbce70) 範囲 `[['00bbce70', '00bbce7f']]`

## 命令位置別の参照

- [`00bbcdd8`](#insn-00bbcdd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcddc`](#insn-00bbcddc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcde0`](#insn-00bbcde0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdec`](#insn-00bbcdec) → `01126460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcdf4`](#insn-00bbcdf4) → [`00bbce44`](#insn-00bbce44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdf8`](#insn-00bbcdf8) → [`00c5d340`](../00c5d/00c5d340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d340` · 推定シンボル `None` · 推定型 `None`
- [`00bbce08`](#insn-00bbce08) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce14`](#insn-00bbce14) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce20`](#insn-00bbce20) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bbce30`](#insn-00bbce30) → [`00c5aee0`](../00c5a/00c5aee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aee0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce3c`](#insn-00bbce3c) → [`00c5ae20`](../00c5a/00c5ae20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae20` · 推定シンボル `None` · 推定型 `None`
- [`00bbce40`](#insn-00bbce40) → [`00bbce70`](#insn-00bbce70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce48`](#insn-00bbce48) → `002a28c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbce4c`](#insn-00bbce4c) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce58`](#insn-00bbce58) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bbce6c`](#insn-00bbce6c) → [`00c5acb0`](../00c5a/00c5acb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5acb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce70`](#insn-00bbce70) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce74`](#insn-00bbce74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbcdd8`](#insn-00bbcdd8)

~~~json
{
  "source": "00bbcdd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcddc`](#insn-00bbcddc)

~~~json
{
  "source": "00bbcddc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcde0`](#insn-00bbcde0)

~~~json
{
  "source": "00bbcde0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdec`](#insn-00bbcdec)

~~~json
{
  "source": "00bbcdec",
  "target": "01126460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126460",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcdf4`](#insn-00bbcdf4)

~~~json
{
  "source": "00bbcdf4",
  "target": "00bbce44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdf8`](#insn-00bbcdf8)

~~~json
{
  "source": "00bbcdf8",
  "target": "00c5d340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce08`](#insn-00bbce08)

~~~json
{
  "source": "00bbce08",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce14`](#insn-00bbce14)

~~~json
{
  "source": "00bbce14",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce20`](#insn-00bbce20)

~~~json
{
  "source": "00bbce20",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce30`](#insn-00bbce30)

~~~json
{
  "source": "00bbce30",
  "target": "00c5aee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce3c`](#insn-00bbce3c)

~~~json
{
  "source": "00bbce3c",
  "target": "00c5ae20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce40`](#insn-00bbce40)

~~~json
{
  "source": "00bbce40",
  "target": "00bbce70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce48`](#insn-00bbce48)

~~~json
{
  "source": "00bbce48",
  "target": "002a28c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a28c8",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a28c8",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbce4c`](#insn-00bbce4c)

~~~json
{
  "source": "00bbce4c",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce58`](#insn-00bbce58)

~~~json
{
  "source": "00bbce58",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce6c`](#insn-00bbce6c)

~~~json
{
  "source": "00bbce6c",
  "target": "00c5acb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce70`](#insn-00bbce70)

~~~json
{
  "source": "00bbce70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce74`](#insn-00bbce74)

~~~json
{
  "source": "00bbce74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
