# 00bdcbfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdbc08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbc08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0010.md#compare-464dcca5c0b26e5b1d84a776afe48527)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcbfc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEiRKS5_",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17c43a04429a38f182a28960e32ae6c6bfc6427b5268e52b1c3da3f742dc0236",
  "source_text_sha256": "17c43a04429a38f182a28960e32ae6c6bfc6427b5268e52b1c3da3f742dc0236",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcbfc",
        "00bdcc9f"
      ]
    ],
    "bytes_sha256": "cb74242b8a8f4323a4eab9ce1ad0d01e3eac95274d846636088fb363f6fb06c9",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5ee80](../00c5e/00c5ee80.md)

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5bee0](../00c5b/00c5bee0.md)
- [00c5ee90](../00c5e/00c5ee90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1111 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEiRKS5_
               (undefined8 param_1,undefined8 param_2,undefined4 param_3,undefined8 param_4)

{
  long lVar1;
  undefined8 uVar2;
  undefined1 auStack_58 [16];
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  uVar2 = _Znwm(0x138);
  _ZN8firebase4auth10AuthResultC2ERKS1_(uVar2,param_4);
                    /* try { // try from 00bdcc4c to 00cdcc5b has its CatchHandler @ 00bdff28 */
                    /* try { // try from 00bdcc5c to 00cdd387 has its CatchHandler @ 00bd7fb0 */
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
            (auStack_58,param_2,param_3,uVar2,
             PTR__ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv_00c9ca88
            );
  _ZN8firebase12FutureHandleC1ERKS0_(param_1,auStack_58);
  _ZN8firebase12FutureHandleD2Ev(auStack_58);
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcbfc"></a> `00bdcbfc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bdcc00"></a> `00bdcc00` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcc04"></a> `00bdcc04` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdcc08"></a> `00bdcc08` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdcc0c"></a> `00bdcc0c` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdcc10"></a> `00bdcc10` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bdcc14"></a> `00bdcc14` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdcc18"></a> `00bdcc18` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdcc1c"></a> `00bdcc1c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bdcc20"></a> `00bdcc20` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdcc24"></a> `00bdcc24` | `00 27 80 52` | mov w0,#0x138 | `FALL_THROUGH`
<a id="insn-00bdcc28"></a> `00bdcc28` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bdcc2c"></a> `00bdcc2c` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00bdcc30"></a> `00bdcc30` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdcc34"></a> `00bdcc34` | `bf f0 01 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcc38"></a> `00bdcc38` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdcc3c"></a> `00bdcc3c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bdcc40"></a> `00bdcc40` | `94 08 02 94` | bl 0x00c5ee90 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcc44"></a> `00bdcc44` | `03 06 00 90` | adrp x3,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bdcc48"></a> `00bdcc48` | `63 44 45 f9` | ldr x3,[x3, #0xa88] | `FALL_THROUGH`
<a id="insn-00bdcc4c"></a> `00bdcc4c` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdcc50"></a> `00bdcc50` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdcc54"></a> `00bdcc54` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00bdcc58"></a> `00bdcc58` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bdcc5c"></a> `00bdcc5c` | `a1 fc 01 94` | bl 0x00c5bee0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcc60"></a> `00bdcc60` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdcc64"></a> `00bdcc64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcc68"></a> `00bdcc68` | `8e fc 01 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcc6c"></a> `00bdcc6c` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdcc70"></a> `00bdcc70` | `b0 fb 01 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcc74"></a> `00bdcc74` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bdcc78"></a> `00bdcc78` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdcc7c"></a> `00bdcc7c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdcc80"></a> `00bdcc80` | `e1 00 00 54` | b.ne 0x00bdcc9c | `CONDITIONAL_JUMP`
<a id="insn-00bdcc84"></a> `00bdcc84` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdcc88"></a> `00bdcc88` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdcc8c"></a> `00bdcc8c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdcc90"></a> `00bdcc90` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcc94"></a> `00bdcc94` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bdcc98"></a> `00bdcc98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdcc9c"></a> `00bdcc9c` | `b9 f0 01 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcbfc`](#insn-00bdcbfc) 範囲 `[['00bdcbfc', '00bdcc4b']]`
  - `FALL_THROUGH` [`00bdcc48`](#insn-00bdcc48) → [`00bdcc4c`](#insn-00bdcc4c)
- ブロック [`00bdcc4c`](#insn-00bdcc4c) 範囲 `[['00bdcc4c', '00bdcc5b']]`
  - `FALL_THROUGH` [`00bdcc58`](#insn-00bdcc58) → [`00bdcc5c`](#insn-00bdcc5c)
- ブロック [`00bdcc5c`](#insn-00bdcc5c) 範囲 `[['00bdcc5c', '00bdcc83']]`
  - `CONDITIONAL_JUMP` [`00bdcc80`](#insn-00bdcc80) → [`00bdcc9c`](#insn-00bdcc9c)
  - `FALL_THROUGH` [`00bdcc80`](#insn-00bdcc80) → [`00bdcc84`](#insn-00bdcc84)
- ブロック [`00bdcc84`](#insn-00bdcc84) 範囲 `[['00bdcc84', '00bdcc9b']]`
- ブロック [`00bdcc9c`](#insn-00bdcc9c) 範囲 `[['00bdcc9c', '00bdcc9f']]`

## 命令位置別の参照

- [`00bdcc00`](#insn-00bdcc00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc04`](#insn-00bdcc04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc08`](#insn-00bdcc08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc0c`](#insn-00bdcc0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc30`](#insn-00bdcc30) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc34`](#insn-00bdcc34) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc40`](#insn-00bdcc40) → [`00c5ee90`](../00c5e/00c5ee90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ee90` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc48`](#insn-00bdcc48) → `00c9ca88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcc48`](#insn-00bdcc48) → [`00bd0d68`](../00bd0/00bd0d68.md) · `PARAM` · `ANALYSIS` · 関数 `00bd0d68` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv` · 推定型 `None`
- [`00bdcc5c`](#insn-00bdcc5c) → [`00c5bee0`](../00c5b/00c5bee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bee0` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc68`](#insn-00bdcc68) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc70`](#insn-00bdcc70) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc78`](#insn-00bdcc78) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc80`](#insn-00bdcc80) → [`00bdcc9c`](#insn-00bdcc9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc84`](#insn-00bdcc84) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc88`](#insn-00bdcc88) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc8c`](#insn-00bdcc8c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc90`](#insn-00bdcc90) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc9c`](#insn-00bdcc9c) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcc00`](#insn-00bdcc00)

~~~json
{
  "source": "00bdcc00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc04`](#insn-00bdcc04)

~~~json
{
  "source": "00bdcc04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc08`](#insn-00bdcc08)

~~~json
{
  "source": "00bdcc08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc0c`](#insn-00bdcc0c)

~~~json
{
  "source": "00bdcc0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc30`](#insn-00bdcc30)

~~~json
{
  "source": "00bdcc30",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc34`](#insn-00bdcc34)

~~~json
{
  "source": "00bdcc34",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcc40`](#insn-00bdcc40)

~~~json
{
  "source": "00bdcc40",
  "target": "00c5ee90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcc48`](#insn-00bdcc48)

~~~json
{
  "source": "00bdcc48",
  "target": "00c9ca88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ca88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcc48`](#insn-00bdcc48)

~~~json
{
  "source": "00bdcc48",
  "target": "00bd0d68",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcc5c`](#insn-00bdcc5c)

~~~json
{
  "source": "00bdcc5c",
  "target": "00c5bee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcc68`](#insn-00bdcc68)

~~~json
{
  "source": "00bdcc68",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcc70`](#insn-00bdcc70)

~~~json
{
  "source": "00bdcc70",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcc78`](#insn-00bdcc78)

~~~json
{
  "source": "00bdcc78",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc80`](#insn-00bdcc80)

~~~json
{
  "source": "00bdcc80",
  "target": "00bdcc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc84`](#insn-00bdcc84)

~~~json
{
  "source": "00bdcc84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc88`](#insn-00bdcc88)

~~~json
{
  "source": "00bdcc88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc8c`](#insn-00bdcc8c)

~~~json
{
  "source": "00bdcc8c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc90`](#insn-00bdcc90)

~~~json
{
  "source": "00bdcc90",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc9c`](#insn-00bdcc9c)

~~~json
{
  "source": "00bdcc9c",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
