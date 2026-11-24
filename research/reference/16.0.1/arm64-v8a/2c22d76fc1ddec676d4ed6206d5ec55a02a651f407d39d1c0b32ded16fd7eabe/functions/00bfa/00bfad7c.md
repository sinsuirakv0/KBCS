# 00bfad7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfa954`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa954.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-9d3bb88803594ec2511c511e60724be5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfae18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfae18.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-4a5a09642d48b5c3882293208ab3fedb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfad7c",
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
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfad7c",
        "00bfae0f"
      ]
    ],
    "bytes_sha256": "d7f0629529423543b01615fde7930242560d9080c45d025590675dc4ed88312d",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c583b0](../00c58/00c583b0.md)

## 呼び出し先

- [00c580c0](../00c58/00c580c0.md)
- [00c58120](../00c58/00c58120.md)
- [00c5d650](../00c5d/00c5d650.md)

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
<a id="insn-00bfad7c"></a> `00bfad7c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfad80"></a> `00bfad80` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bfad84"></a> `00bfad84` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfad88"></a> `00bfad88` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfad8c"></a> `00bfad8c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfad90"></a> `00bfad90` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfad94"></a> `00bfad94` | `b4 73 00 91` | add x20,x29,#0x1c | `FALL_THROUGH`
<a id="insn-00bfad98"></a> `00bfad98` | `95 00 80 52` | mov w21,#0x4 | `FALL_THROUGH`
<a id="insn-00bfad9c"></a> `00bfad9c` | `06 00 00 14` | b 0x00bfadb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfada0"></a> `00bfada0` | `c8 74 01 94` | bl 0x00c580c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfada4"></a> `00bfada4` | `00 00 40 b9` | ldr w0,[x0] | `FALL_THROUGH`
<a id="insn-00bfada8"></a> `00bfada8` | `1f 10 00 71` | cmp w0,#0x4 | `FALL_THROUGH`
<a id="insn-00bfadac"></a> `00bfadac` | `41 02 00 54` | b.ne 0x00bfadf4 | `CONDITIONAL_JUMP`
<a id="insn-00bfadb0"></a> `00bfadb0` | `75 01 00 b4` | cbz x21,0x00bfaddc | `CONDITIONAL_JUMP`
<a id="insn-00bfadb4"></a> `00bfadb4` | `60 02 40 b9` | ldr w0,[x19] | `FALL_THROUGH`
<a id="insn-00bfadb8"></a> `00bfadb8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfadbc"></a> `00bfadbc` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bfadc0"></a> `00bfadc0` | `24 8a 01 94` | bl 0x00c5d650 | `UNCONDITIONAL_CALL`
<a id="insn-00bfadc4"></a> `00bfadc4` | `1f 04 00 b1` | cmn x0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfadc8"></a> `00bfadc8` | `c0 fe ff 54` | b.eq 0x00bfada0 | `CONDITIONAL_JUMP`
<a id="insn-00bfadcc"></a> `00bfadcc` | `a0 01 00 b4` | cbz x0,0x00bfae00 | `CONDITIONAL_JUMP`
<a id="insn-00bfadd0"></a> `00bfadd0` | `b5 02 00 cb` | sub x21,x21,x0 | `FALL_THROUGH`
<a id="insn-00bfadd4"></a> `00bfadd4` | `94 02 00 8b` | add x20,x20,x0 | `FALL_THROUGH`
<a id="insn-00bfadd8"></a> `00bfadd8` | `f5 fe ff b5` | cbnz x21,0x00bfadb4 | `CONDITIONAL_JUMP`
<a id="insn-00bfaddc"></a> `00bfaddc` | `a0 1f 40 b9` | ldr w0,[x29, #0x1c] | `FALL_THROUGH`
<a id="insn-00bfade0"></a> `00bfade0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfade4"></a> `00bfade4` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfade8"></a> `00bfade8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfadec"></a> `00bfadec` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfadf0"></a> `00bfadf0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfadf4"></a> `00bfadf4` | `e1 b5 ff d0` | adrp x1,0x2b8000 | `FALL_THROUGH`
<a id="insn-00bfadf8"></a> `00bfadf8` | `21 08 35 91` | add x1,x1,#0xd42 | `FALL_THROUGH`
<a id="insn-00bfadfc"></a> `00bfadfc` | `c9 74 01 94` | bl 0x00c58120 | `CALL_TERMINATOR`
<a id="insn-00bfae00"></a> `00bfae00` | `81 b5 ff d0` | adrp x1,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bfae04"></a> `00bfae04` | `21 ac 12 91` | add x1,x1,#0x4ab | `FALL_THROUGH`
<a id="insn-00bfae08"></a> `00bfae08` | `a0 07 80 52` | mov w0,#0x3d | `FALL_THROUGH`
<a id="insn-00bfae0c"></a> `00bfae0c` | `c5 74 01 94` | bl 0x00c58120 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfad7c`](#insn-00bfad7c) 範囲 `[['00bfad7c', '00bfad9f']]`
  - `UNCONDITIONAL_JUMP` [`00bfad9c`](#insn-00bfad9c) → [`00bfadb4`](#insn-00bfadb4)
- ブロック [`00bfada0`](#insn-00bfada0) 範囲 `[['00bfada0', '00bfadaf']]`
  - `CONDITIONAL_JUMP` [`00bfadac`](#insn-00bfadac) → [`00bfadf4`](#insn-00bfadf4)
  - `FALL_THROUGH` [`00bfadac`](#insn-00bfadac) → [`00bfadb0`](#insn-00bfadb0)
- ブロック [`00bfadb0`](#insn-00bfadb0) 範囲 `[['00bfadb0', '00bfadb3']]`
  - `CONDITIONAL_JUMP` [`00bfadb0`](#insn-00bfadb0) → [`00bfaddc`](#insn-00bfaddc)
  - `FALL_THROUGH` [`00bfadb0`](#insn-00bfadb0) → [`00bfadb4`](#insn-00bfadb4)
- ブロック [`00bfadb4`](#insn-00bfadb4) 範囲 `[['00bfadb4', '00bfadcb']]`
  - `CONDITIONAL_JUMP` [`00bfadc8`](#insn-00bfadc8) → [`00bfada0`](#insn-00bfada0)
  - `FALL_THROUGH` [`00bfadc8`](#insn-00bfadc8) → [`00bfadcc`](#insn-00bfadcc)
- ブロック [`00bfadcc`](#insn-00bfadcc) 範囲 `[['00bfadcc', '00bfadcf']]`
  - `CONDITIONAL_JUMP` [`00bfadcc`](#insn-00bfadcc) → [`00bfae00`](#insn-00bfae00)
  - `FALL_THROUGH` [`00bfadcc`](#insn-00bfadcc) → [`00bfadd0`](#insn-00bfadd0)
- ブロック [`00bfadd0`](#insn-00bfadd0) 範囲 `[['00bfadd0', '00bfaddb']]`
  - `CONDITIONAL_JUMP` [`00bfadd8`](#insn-00bfadd8) → [`00bfadb4`](#insn-00bfadb4)
  - `FALL_THROUGH` [`00bfadd8`](#insn-00bfadd8) → [`00bfaddc`](#insn-00bfaddc)
- ブロック [`00bfaddc`](#insn-00bfaddc) 範囲 `[['00bfaddc', '00bfadf3']]`
- ブロック [`00bfadf4`](#insn-00bfadf4) 範囲 `[['00bfadf4', '00bfadff']]`
- ブロック [`00bfae00`](#insn-00bfae00) 範囲 `[['00bfae00', '00bfae0f']]`

## 命令位置別の参照

- [`00bfad80`](#insn-00bfad80) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfad84`](#insn-00bfad84) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfad88`](#insn-00bfad88) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfad9c`](#insn-00bfad9c) → [`00bfadb4`](#insn-00bfadb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfada0`](#insn-00bfada0) → [`00c580c0`](../00c58/00c580c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580c0` · 推定シンボル `None` · 推定型 `None`
- [`00bfadac`](#insn-00bfadac) → [`00bfadf4`](#insn-00bfadf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfadb0`](#insn-00bfadb0) → [`00bfaddc`](#insn-00bfaddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfadc0`](#insn-00bfadc0) → [`00c5d650`](../00c5d/00c5d650.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d650` · 推定シンボル `None` · 推定型 `None`
- [`00bfadc8`](#insn-00bfadc8) → [`00bfada0`](#insn-00bfada0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfadcc`](#insn-00bfadcc) → [`00bfae00`](#insn-00bfae00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfadd8`](#insn-00bfadd8) → [`00bfadb4`](#insn-00bfadb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaddc`](#insn-00bfaddc) → `Stack[-0x14]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfade0`](#insn-00bfade0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfade4`](#insn-00bfade4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfade8`](#insn-00bfade8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfadf8`](#insn-00bfadf8) → `002b8d42`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfadfc`](#insn-00bfadfc) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bfae04`](#insn-00bfae04) → `002ac4ab`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfae0c`](#insn-00bfae0c) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfad80`](#insn-00bfad80)

~~~json
{
  "source": "00bfad80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfad84`](#insn-00bfad84)

~~~json
{
  "source": "00bfad84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfad88`](#insn-00bfad88)

~~~json
{
  "source": "00bfad88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfad9c`](#insn-00bfad9c)

~~~json
{
  "source": "00bfad9c",
  "target": "00bfadb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfada0`](#insn-00bfada0)

~~~json
{
  "source": "00bfada0",
  "target": "00c580c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfadac`](#insn-00bfadac)

~~~json
{
  "source": "00bfadac",
  "target": "00bfadf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfadb0`](#insn-00bfadb0)

~~~json
{
  "source": "00bfadb0",
  "target": "00bfaddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfadc0`](#insn-00bfadc0)

~~~json
{
  "source": "00bfadc0",
  "target": "00c5d650",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfadc8`](#insn-00bfadc8)

~~~json
{
  "source": "00bfadc8",
  "target": "00bfada0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfadcc`](#insn-00bfadcc)

~~~json
{
  "source": "00bfadcc",
  "target": "00bfae00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfadd8`](#insn-00bfadd8)

~~~json
{
  "source": "00bfadd8",
  "target": "00bfadb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaddc`](#insn-00bfaddc)

~~~json
{
  "source": "00bfaddc",
  "target": "Stack[-0x14]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfade0`](#insn-00bfade0)

~~~json
{
  "source": "00bfade0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfade4`](#insn-00bfade4)

~~~json
{
  "source": "00bfade4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfade8`](#insn-00bfade8)

~~~json
{
  "source": "00bfade8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfadf8`](#insn-00bfadf8)

~~~json
{
  "source": "00bfadf8",
  "target": "002b8d42",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8d42",
  "offset": 0,
  "size": 38,
  "datatype": "string",
  "bytes": "72616e646f6d5f64657669636520676f7420616e20756e657870656374656420",
  "capture_start": "002b8d42",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bfadfc`](#insn-00bfadfc)

~~~json
{
  "source": "00bfadfc",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfae04`](#insn-00bfae04)

~~~json
{
  "source": "00bfae04",
  "target": "002ac4ab",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac4ab",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "72616e646f6d5f64657669636520676f7420454f4600",
  "capture_start": "002ac4ab",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfae0c`](#insn-00bfae0c)

~~~json
{
  "source": "00bfae0c",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
