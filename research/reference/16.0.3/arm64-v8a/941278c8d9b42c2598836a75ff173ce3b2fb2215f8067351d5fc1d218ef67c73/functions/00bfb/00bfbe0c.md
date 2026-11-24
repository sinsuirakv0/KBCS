# 00bfbe0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfae18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfae18.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-9d156ec223852fadaf2b9312b98f432e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbe0c",
  "name": "_ZNSt6__ndk113random_deviceclEv",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f55d05815ca45746b9f4cdbcbc5f6056326da19f6aedac0478140bd7c8dadfc",
  "source_text_sha256": "8f55d05815ca45746b9f4cdbcbc5f6056326da19f6aedac0478140bd7c8dadfc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbe0c",
        "00bfbe9f"
      ]
    ],
    "bytes_sha256": "c167ed84ccc55428d3d387059ca16d027be1bf788a00fc0ae8cb17deae2d06d0",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c59450](../00c59/00c59450.md)

## 呼び出し先

- [00c59160](../00c59/00c59160.md)
- [00c591c0](../00c59/00c591c0.md)
- [00c5e6f0](../00c5e/00c5e6f0.md)

## 関連文字列（未確認候補）

~~~text
"random_device got EOF"
"random_device got an unexpected error"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 861 bytes

~~~c

undefined4 _ZNSt6__ndk113random_deviceclEv(int *param_1)

{
  int *piVar1;
  ssize_t sVar2;
  undefined4 *__buf;
  size_t __nbytes;
  undefined4 local_14;
  
  __buf = &local_14;
  __nbytes = 4;
  do {
    while (sVar2 = read(*param_1,__buf,__nbytes), sVar2 != -1) {
      if (sVar2 == 0) {
                    /* WARNING: Subroutine does not return */
        _ZNSt6__ndk120__throw_system_errorEiPKc(0x3d,"random_device got EOF");
      }
      __nbytes = __nbytes - sVar2;
      __buf = (undefined4 *)((long)__buf + sVar2);
      if (__nbytes == 0) {
        return local_14;
      }
    }
    piVar1 = (int *)__errno();
    if (*piVar1 != 4) {
                    /* WARNING: Subroutine does not return */
      _ZNSt6__ndk120__throw_system_errorEiPKc(*piVar1,"random_device got an unexpected error");
    }
  } while (__nbytes != 0);
  return local_14;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbe0c"></a> `00bfbe0c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbe10"></a> `00bfbe10` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bfbe14"></a> `00bfbe14` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbe18"></a> `00bfbe18` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbe1c"></a> `00bfbe1c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbe20"></a> `00bfbe20` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfbe24"></a> `00bfbe24` | `b4 73 00 91` | add x20,x29,#0x1c | `FALL_THROUGH`
<a id="insn-00bfbe28"></a> `00bfbe28` | `95 00 80 52` | mov w21,#0x4 | `FALL_THROUGH`
<a id="insn-00bfbe2c"></a> `00bfbe2c` | `06 00 00 14` | b 0x00bfbe44 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfbe30"></a> `00bfbe30` | `cc 74 01 94` | bl 0x00c59160 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbe34"></a> `00bfbe34` | `00 00 40 b9` | ldr w0,[x0] | `FALL_THROUGH`
<a id="insn-00bfbe38"></a> `00bfbe38` | `1f 10 00 71` | cmp w0,#0x4 | `FALL_THROUGH`
<a id="insn-00bfbe3c"></a> `00bfbe3c` | `41 02 00 54` | b.ne 0x00bfbe84 | `CONDITIONAL_JUMP`
<a id="insn-00bfbe40"></a> `00bfbe40` | `75 01 00 b4` | cbz x21,0x00bfbe6c | `CONDITIONAL_JUMP`
<a id="insn-00bfbe44"></a> `00bfbe44` | `60 02 40 b9` | ldr w0,[x19] | `FALL_THROUGH`
<a id="insn-00bfbe48"></a> `00bfbe48` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfbe4c"></a> `00bfbe4c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bfbe50"></a> `00bfbe50` | `28 8a 01 94` | bl 0x00c5e6f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbe54"></a> `00bfbe54` | `1f 04 00 b1` | cmn x0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfbe58"></a> `00bfbe58` | `c0 fe ff 54` | b.eq 0x00bfbe30 | `CONDITIONAL_JUMP`
<a id="insn-00bfbe5c"></a> `00bfbe5c` | `a0 01 00 b4` | cbz x0,0x00bfbe90 | `CONDITIONAL_JUMP`
<a id="insn-00bfbe60"></a> `00bfbe60` | `b5 02 00 cb` | sub x21,x21,x0 | `FALL_THROUGH`
<a id="insn-00bfbe64"></a> `00bfbe64` | `94 02 00 8b` | add x20,x20,x0 | `FALL_THROUGH`
<a id="insn-00bfbe68"></a> `00bfbe68` | `f5 fe ff b5` | cbnz x21,0x00bfbe44 | `CONDITIONAL_JUMP`
<a id="insn-00bfbe6c"></a> `00bfbe6c` | `a0 1f 40 b9` | ldr w0,[x29, #0x1c] | `FALL_THROUGH`
<a id="insn-00bfbe70"></a> `00bfbe70` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbe74"></a> `00bfbe74` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbe78"></a> `00bfbe78` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfbe7c"></a> `00bfbe7c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbe80"></a> `00bfbe80` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfbe84"></a> `00bfbe84` | `e1 b5 ff b0` | adrp x1,0x2b8000 | `FALL_THROUGH`
<a id="insn-00bfbe88"></a> `00bfbe88` | `21 f4 36 91` | add x1,x1,#0xdbd | `FALL_THROUGH`
<a id="insn-00bfbe8c"></a> `00bfbe8c` | `cd 74 01 94` | bl 0x00c591c0 | `CALL_TERMINATOR`
<a id="insn-00bfbe90"></a> `00bfbe90` | `81 b5 ff b0` | adrp x1,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bfbe94"></a> `00bfbe94` | `21 70 14 91` | add x1,x1,#0x51c | `FALL_THROUGH`
<a id="insn-00bfbe98"></a> `00bfbe98` | `a0 07 80 52` | mov w0,#0x3d | `FALL_THROUGH`
<a id="insn-00bfbe9c"></a> `00bfbe9c` | `c9 74 01 94` | bl 0x00c591c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbe0c`](#insn-00bfbe0c) 範囲 `[['00bfbe0c', '00bfbe2f']]`
  - `UNCONDITIONAL_JUMP` [`00bfbe2c`](#insn-00bfbe2c) → [`00bfbe44`](#insn-00bfbe44)
- ブロック [`00bfbe30`](#insn-00bfbe30) 範囲 `[['00bfbe30', '00bfbe3f']]`
  - `CONDITIONAL_JUMP` [`00bfbe3c`](#insn-00bfbe3c) → [`00bfbe84`](#insn-00bfbe84)
  - `FALL_THROUGH` [`00bfbe3c`](#insn-00bfbe3c) → [`00bfbe40`](#insn-00bfbe40)
- ブロック [`00bfbe40`](#insn-00bfbe40) 範囲 `[['00bfbe40', '00bfbe43']]`
  - `CONDITIONAL_JUMP` [`00bfbe40`](#insn-00bfbe40) → [`00bfbe6c`](#insn-00bfbe6c)
  - `FALL_THROUGH` [`00bfbe40`](#insn-00bfbe40) → [`00bfbe44`](#insn-00bfbe44)
- ブロック [`00bfbe44`](#insn-00bfbe44) 範囲 `[['00bfbe44', '00bfbe5b']]`
  - `CONDITIONAL_JUMP` [`00bfbe58`](#insn-00bfbe58) → [`00bfbe30`](#insn-00bfbe30)
  - `FALL_THROUGH` [`00bfbe58`](#insn-00bfbe58) → [`00bfbe5c`](#insn-00bfbe5c)
- ブロック [`00bfbe5c`](#insn-00bfbe5c) 範囲 `[['00bfbe5c', '00bfbe5f']]`
  - `CONDITIONAL_JUMP` [`00bfbe5c`](#insn-00bfbe5c) → [`00bfbe90`](#insn-00bfbe90)
  - `FALL_THROUGH` [`00bfbe5c`](#insn-00bfbe5c) → [`00bfbe60`](#insn-00bfbe60)
- ブロック [`00bfbe60`](#insn-00bfbe60) 範囲 `[['00bfbe60', '00bfbe6b']]`
  - `CONDITIONAL_JUMP` [`00bfbe68`](#insn-00bfbe68) → [`00bfbe44`](#insn-00bfbe44)
  - `FALL_THROUGH` [`00bfbe68`](#insn-00bfbe68) → [`00bfbe6c`](#insn-00bfbe6c)
- ブロック [`00bfbe6c`](#insn-00bfbe6c) 範囲 `[['00bfbe6c', '00bfbe83']]`
- ブロック [`00bfbe84`](#insn-00bfbe84) 範囲 `[['00bfbe84', '00bfbe8f']]`
- ブロック [`00bfbe90`](#insn-00bfbe90) 範囲 `[['00bfbe90', '00bfbe9f']]`

## 命令位置別の参照

- [`00bfbe10`](#insn-00bfbe10) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe14`](#insn-00bfbe14) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe18`](#insn-00bfbe18) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe2c`](#insn-00bfbe2c) → [`00bfbe44`](#insn-00bfbe44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe30`](#insn-00bfbe30) → [`00c59160`](../00c59/00c59160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59160` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe3c`](#insn-00bfbe3c) → [`00bfbe84`](#insn-00bfbe84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe40`](#insn-00bfbe40) → [`00bfbe6c`](#insn-00bfbe6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe50`](#insn-00bfbe50) → [`00c5e6f0`](../00c5e/00c5e6f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e6f0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe58`](#insn-00bfbe58) → [`00bfbe30`](#insn-00bfbe30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe5c`](#insn-00bfbe5c) → [`00bfbe90`](#insn-00bfbe90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe68`](#insn-00bfbe68) → [`00bfbe44`](#insn-00bfbe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe6c`](#insn-00bfbe6c) → `Stack[-0x14]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe70`](#insn-00bfbe70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe74`](#insn-00bfbe74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe78`](#insn-00bfbe78) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe88`](#insn-00bfbe88) → `002b8dbd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfbe8c`](#insn-00bfbe8c) → [`00c591c0`](../00c59/00c591c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c591c0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe94`](#insn-00bfbe94) → `002ac51c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfbe9c`](#insn-00bfbe9c) → [`00c591c0`](../00c59/00c591c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c591c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbe10`](#insn-00bfbe10)

~~~json
{
  "source": "00bfbe10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe14`](#insn-00bfbe14)

~~~json
{
  "source": "00bfbe14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe18`](#insn-00bfbe18)

~~~json
{
  "source": "00bfbe18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe2c`](#insn-00bfbe2c)

~~~json
{
  "source": "00bfbe2c",
  "target": "00bfbe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe30`](#insn-00bfbe30)

~~~json
{
  "source": "00bfbe30",
  "target": "00c59160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbe3c`](#insn-00bfbe3c)

~~~json
{
  "source": "00bfbe3c",
  "target": "00bfbe84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe40`](#insn-00bfbe40)

~~~json
{
  "source": "00bfbe40",
  "target": "00bfbe6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe50`](#insn-00bfbe50)

~~~json
{
  "source": "00bfbe50",
  "target": "00c5e6f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbe58`](#insn-00bfbe58)

~~~json
{
  "source": "00bfbe58",
  "target": "00bfbe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe5c`](#insn-00bfbe5c)

~~~json
{
  "source": "00bfbe5c",
  "target": "00bfbe90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe68`](#insn-00bfbe68)

~~~json
{
  "source": "00bfbe68",
  "target": "00bfbe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe6c`](#insn-00bfbe6c)

~~~json
{
  "source": "00bfbe6c",
  "target": "Stack[-0x14]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe70`](#insn-00bfbe70)

~~~json
{
  "source": "00bfbe70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe74`](#insn-00bfbe74)

~~~json
{
  "source": "00bfbe74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe78`](#insn-00bfbe78)

~~~json
{
  "source": "00bfbe78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe88`](#insn-00bfbe88)

~~~json
{
  "source": "00bfbe88",
  "target": "002b8dbd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8dbd",
  "offset": 0,
  "size": 38,
  "datatype": "string",
  "bytes": "72616e646f6d5f64657669636520676f7420616e20756e657870656374656420",
  "capture_start": "002b8dbd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bfbe8c`](#insn-00bfbe8c)

~~~json
{
  "source": "00bfbe8c",
  "target": "00c591c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbe94`](#insn-00bfbe94)

~~~json
{
  "source": "00bfbe94",
  "target": "002ac51c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac51c",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "72616e646f6d5f64657669636520676f7420454f4600",
  "capture_start": "002ac51c",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfbe9c`](#insn-00bfbe9c)

~~~json
{
  "source": "00bfbe9c",
  "target": "00c591c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
