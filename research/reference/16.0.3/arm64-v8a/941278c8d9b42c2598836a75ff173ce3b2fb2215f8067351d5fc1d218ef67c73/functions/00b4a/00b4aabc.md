# 00b4aabc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b49ac8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49ac8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0074.md#compare-ec091a733488cbd2c0c2f92e8f1ead55)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4aabc",
  "name": "_ZN8firebase4util6cursor12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c3cbbabe6f8f0b7dee8fc091fcd2107cc885076f7ec09c7124e6aa492cb224f7",
  "source_text_sha256": "c3cbbabe6f8f0b7dee8fc091fcd2107cc885076f7ec09c7124e6aa492cb224f7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4aabc",
        "00b4ab5b"
      ]
    ],
    "bytes_sha256": "c4a0c93d7ae543c8bee6f17a090fe5fa8389e23dfd3ae35da8edf2be915b6546",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 603 bytes

~~~c

void _ZN8firebase4util6cursor12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_01126a98 != 0) {
    if (DAT_01126aa0 != '\0') {
                    /* try { // try from 00b4aaec to 00c4aaf7 has its CatchHandler @ 00b500c4 */
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126aa0 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126a98);
    DAT_01126a98 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4aabc"></a> `00b4aabc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b4aac0"></a> `00b4aac0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4aac4"></a> `00b4aac4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4aac8"></a> `00b4aac8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b4aacc"></a> `00b4aacc` | `f4 2e 00 90` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00b4aad0"></a> `00b4aad0` | `81 4e 45 f9` | ldr x1,[x20, #0xa98] | `FALL_THROUGH`
<a id="insn-00b4aad4"></a> `00b4aad4` | `c1 03 00 b4` | cbz x1,0x00b4ab4c | `CONDITIONAL_JUMP`
<a id="insn-00b4aad8"></a> `00b4aad8` | `f5 2e 00 90` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00b4aadc"></a> `00b4aadc` | `a8 82 6a 39` | ldrb w8,[x21, #0xaa0] | `FALL_THROUGH`
<a id="insn-00b4aae0"></a> `00b4aae0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4aae4"></a> `00b4aae4` | `c8 00 00 34` | cbz w8,0x00b4aafc | `CONDITIONAL_JUMP`
<a id="insn-00b4aae8"></a> `00b4aae8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4aaec"></a> `00b4aaec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4aaf0"></a> `00b4aaf0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00b4aaf4"></a> `00b4aaf4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4aaf8"></a> `00b4aaf8` | `bf 82 2a 39` | strb wzr,[x21, #0xaa0] | `FALL_THROUGH`
<a id="insn-00b4aafc"></a> `00b4aafc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4ab00"></a> `00b4ab00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4ab04"></a> `00b4ab04` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00b4ab08"></a> `00b4ab08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4ab0c"></a> `00b4ab0c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00b4ab10"></a> `00b4ab10` | `20 01 00 54` | b.eq 0x00b4ab34 | `CONDITIONAL_JUMP`
<a id="insn-00b4ab14"></a> `00b4ab14` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4ab18"></a> `00b4ab18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4ab1c"></a> `00b4ab1c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00b4ab20"></a> `00b4ab20` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4ab24"></a> `00b4ab24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4ab28"></a> `00b4ab28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4ab2c"></a> `00b4ab2c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00b4ab30"></a> `00b4ab30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4ab34"></a> `00b4ab34` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4ab38"></a> `00b4ab38` | `81 4e 45 f9` | ldr x1,[x20, #0xa98] | `FALL_THROUGH`
<a id="insn-00b4ab3c"></a> `00b4ab3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4ab40"></a> `00b4ab40` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00b4ab44"></a> `00b4ab44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4ab48"></a> `00b4ab48` | `9f 4e 05 f9` | str xzr,[x20, #0xa98] | `FALL_THROUGH`
<a id="insn-00b4ab4c"></a> `00b4ab4c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4ab50"></a> `00b4ab50` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4ab54"></a> `00b4ab54` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b4ab58"></a> `00b4ab58` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4aabc`](#insn-00b4aabc) 範囲 `[['00b4aabc', '00b4aad7']]`
  - `CONDITIONAL_JUMP` [`00b4aad4`](#insn-00b4aad4) → [`00b4ab4c`](#insn-00b4ab4c)
  - `FALL_THROUGH` [`00b4aad4`](#insn-00b4aad4) → [`00b4aad8`](#insn-00b4aad8)
- ブロック [`00b4aad8`](#insn-00b4aad8) 範囲 `[['00b4aad8', '00b4aae7']]`
  - `CONDITIONAL_JUMP` [`00b4aae4`](#insn-00b4aae4) → [`00b4aafc`](#insn-00b4aafc)
  - `FALL_THROUGH` [`00b4aae4`](#insn-00b4aae4) → [`00b4aae8`](#insn-00b4aae8)
- ブロック [`00b4aae8`](#insn-00b4aae8) 範囲 `[['00b4aae8', '00b4aaeb']]`
  - `FALL_THROUGH` [`00b4aae8`](#insn-00b4aae8) → [`00b4aaec`](#insn-00b4aaec)
- ブロック [`00b4aaec`](#insn-00b4aaec) 範囲 `[['00b4aaec', '00b4aafb']]`
  - `FALL_THROUGH` [`00b4aaf8`](#insn-00b4aaf8) → [`00b4aafc`](#insn-00b4aafc)
- ブロック [`00b4aafc`](#insn-00b4aafc) 範囲 `[['00b4aafc', '00b4ab13']]`
  - `CONDITIONAL_JUMP` [`00b4ab10`](#insn-00b4ab10) → [`00b4ab34`](#insn-00b4ab34)
  - `FALL_THROUGH` [`00b4ab10`](#insn-00b4ab10) → [`00b4ab14`](#insn-00b4ab14)
- ブロック [`00b4ab14`](#insn-00b4ab14) 範囲 `[['00b4ab14', '00b4ab33']]`
  - `FALL_THROUGH` [`00b4ab30`](#insn-00b4ab30) → [`00b4ab34`](#insn-00b4ab34)
- ブロック [`00b4ab34`](#insn-00b4ab34) 範囲 `[['00b4ab34', '00b4ab4b']]`
  - `FALL_THROUGH` [`00b4ab48`](#insn-00b4ab48) → [`00b4ab4c`](#insn-00b4ab4c)
- ブロック [`00b4ab4c`](#insn-00b4ab4c) 範囲 `[['00b4ab4c', '00b4ab5b']]`

## 命令位置別の参照

- [`00b4aabc`](#insn-00b4aabc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aac0`](#insn-00b4aac0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aac4`](#insn-00b4aac4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aad0`](#insn-00b4aad0) → `01126a98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4aad4`](#insn-00b4aad4) → [`00b4ab4c`](#insn-00b4ab4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aadc`](#insn-00b4aadc) → `01126aa0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4aae4`](#insn-00b4aae4) → [`00b4aafc`](#insn-00b4aafc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aaf8`](#insn-00b4aaf8) → `01126aa0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4ab10`](#insn-00b4ab10) → [`00b4ab34`](#insn-00b4ab34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ab38`](#insn-00b4ab38) → `01126a98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ab48`](#insn-00b4ab48) → `01126a98`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ab4c`](#insn-00b4ab4c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ab50`](#insn-00b4ab50) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4aabc`](#insn-00b4aabc)

~~~json
{
  "source": "00b4aabc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aac0`](#insn-00b4aac0)

~~~json
{
  "source": "00b4aac0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aac4`](#insn-00b4aac4)

~~~json
{
  "source": "00b4aac4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aad0`](#insn-00b4aad0)

~~~json
{
  "source": "00b4aad0",
  "target": "01126a98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4aad4`](#insn-00b4aad4)

~~~json
{
  "source": "00b4aad4",
  "target": "00b4ab4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aadc`](#insn-00b4aadc)

~~~json
{
  "source": "00b4aadc",
  "target": "01126aa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126aa0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4aae4`](#insn-00b4aae4)

~~~json
{
  "source": "00b4aae4",
  "target": "00b4aafc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aaf8`](#insn-00b4aaf8)

~~~json
{
  "source": "00b4aaf8",
  "target": "01126aa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126aa0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ab10`](#insn-00b4ab10)

~~~json
{
  "source": "00b4ab10",
  "target": "00b4ab34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ab38`](#insn-00b4ab38)

~~~json
{
  "source": "00b4ab38",
  "target": "01126a98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ab48`](#insn-00b4ab48)

~~~json
{
  "source": "00b4ab48",
  "target": "01126a98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ab4c`](#insn-00b4ab4c)

~~~json
{
  "source": "00b4ab4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ab50`](#insn-00b4ab50)

~~~json
{
  "source": "00b4ab50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
