# 00afbadc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afbba4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbba4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-f29036221751e5c89086e4e0968702ab)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbadc",
  "name": "_ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3ba0cdb4831309a5362a50af0c188d6a2bbdf7fe91a6e96776a8e7ecddee8356",
  "source_text_sha256": "3ba0cdb4831309a5362a50af0c188d6a2bbdf7fe91a6e96776a8e7ecddee8356",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbadc",
        "00afbb63"
      ]
    ],
    "bytes_sha256": "ac90c26e7ee8eb6d14792739f3d5fd42ad6fbac509861416ae02ed18136d823f",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb6d0](../00bdb/00bdb6d0.md)
- [00bdeb30](../00bde/00bdeb30.md)
- [00bdeb90](../00bde/00bdeb90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 995 bytes

~~~c

undefined8 _ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE(long *param_1)

{
  int iVar1;
  pthread_t __thread1;
  undefined8 uVar2;
  
  if (DAT_010a0c38 == '\x01') {
    __thread1 = pthread_self();
                    /* try { // try from 00afbb00 to 00bfbb07 has its CatchHandler @ 00aff428 */
    if ((__thread1 == 0) || (DAT_010a0c40 == 0)) {
      if (DAT_010a0c40 != 0 || __thread1 != 0) goto LAB_00afbb54;
    }
    else {
      iVar1 = pthread_equal(__thread1,DAT_010a0c40);
      if (iVar1 == 0) goto LAB_00afbb54;
    }
    (**(code **)(*param_1 + 0x10))(param_1);
    if (param_1 != (long *)0x0) {
                    /* try { // try from 00afbb30 to 00bfbb47 has its CatchHandler @ 00aff424 */
      (**(code **)(*param_1 + 8))(param_1);
    }
    return 0;
  }
LAB_00afbb54:
                    /* try { // try from 00afbb58 to 00bfbb6f has its CatchHandler @ 00b0037c */
  uVar2 = _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE(param_1);
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbadc"></a> `00afbadc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afbae0"></a> `00afbae0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbae4"></a> `00afbae4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00afbae8"></a> `00afbae8` | `28 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbaec"></a> `00afbaec` | `08 e1 70 39` | ldrb w8,[x8, #0xc38] | `FALL_THROUGH`
<a id="insn-00afbaf0"></a> `00afbaf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afbaf4"></a> `00afbaf4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afbaf8"></a> `00afbaf8` | `e1 02 00 54` | b.ne 0x00afbb54 | `CONDITIONAL_JUMP`
<a id="insn-00afbafc"></a> `00afbafc` | `f5 7e 03 94` | bl 0x00bdb6d0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbb00"></a> `00afbb00` | `28 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbb04"></a> `00afbb04` | `01 21 46 f9` | ldr x1,[x8, #0xc40] | `FALL_THROUGH`
<a id="insn-00afbb08"></a> `00afbb08` | `20 02 00 b4` | cbz x0,0x00afbb4c | `CONDITIONAL_JUMP`
<a id="insn-00afbb0c"></a> `00afbb0c` | `01 02 00 b4` | cbz x1,0x00afbb4c | `CONDITIONAL_JUMP`
<a id="insn-00afbb10"></a> `00afbb10` | `20 8c 03 94` | bl 0x00bdeb90 | `UNCONDITIONAL_CALL`
<a id="insn-00afbb14"></a> `00afbb14` | `00 02 00 34` | cbz w0,0x00afbb54 | `CONDITIONAL_JUMP`
<a id="insn-00afbb18"></a> `00afbb18` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00afbb1c"></a> `00afbb1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbb20"></a> `00afbb20` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afbb24"></a> `00afbb24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afbb28"></a> `00afbb28` | `b3 00 00 b4` | cbz x19,0x00afbb3c | `CONDITIONAL_JUMP`
<a id="insn-00afbb2c"></a> `00afbb2c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00afbb30"></a> `00afbb30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbb34"></a> `00afbb34` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afbb38"></a> `00afbb38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afbb3c"></a> `00afbb3c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbb40"></a> `00afbb40` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00afbb44"></a> `00afbb44` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afbb48"></a> `00afbb48` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afbb4c"></a> `00afbb4c` | `28 00 00 aa` | orr x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00afbb50"></a> `00afbb50` | `48 fe ff b4` | cbz x8,0x00afbb18 | `CONDITIONAL_JUMP`
<a id="insn-00afbb54"></a> `00afbb54` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbb58"></a> `00afbb58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbb5c"></a> `00afbb5c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afbb60"></a> `00afbb60` | `f4 8b 03 14` | b 0x00bdeb30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbadc`](#insn-00afbadc) 範囲 `[['00afbadc', '00afbafb']]`
  - `CONDITIONAL_JUMP` [`00afbaf8`](#insn-00afbaf8) → [`00afbb54`](#insn-00afbb54)
  - `FALL_THROUGH` [`00afbaf8`](#insn-00afbaf8) → [`00afbafc`](#insn-00afbafc)
- ブロック [`00afbafc`](#insn-00afbafc) 範囲 `[['00afbafc', '00afbaff']]`
  - `FALL_THROUGH` [`00afbafc`](#insn-00afbafc) → [`00afbb00`](#insn-00afbb00)
- ブロック [`00afbb00`](#insn-00afbb00) 範囲 `[['00afbb00', '00afbb0b']]`
  - `CONDITIONAL_JUMP` [`00afbb08`](#insn-00afbb08) → [`00afbb4c`](#insn-00afbb4c)
  - `FALL_THROUGH` [`00afbb08`](#insn-00afbb08) → [`00afbb0c`](#insn-00afbb0c)
- ブロック [`00afbb0c`](#insn-00afbb0c) 範囲 `[['00afbb0c', '00afbb0f']]`
  - `CONDITIONAL_JUMP` [`00afbb0c`](#insn-00afbb0c) → [`00afbb4c`](#insn-00afbb4c)
  - `FALL_THROUGH` [`00afbb0c`](#insn-00afbb0c) → [`00afbb10`](#insn-00afbb10)
- ブロック [`00afbb10`](#insn-00afbb10) 範囲 `[['00afbb10', '00afbb17']]`
  - `CONDITIONAL_JUMP` [`00afbb14`](#insn-00afbb14) → [`00afbb54`](#insn-00afbb54)
  - `FALL_THROUGH` [`00afbb14`](#insn-00afbb14) → [`00afbb18`](#insn-00afbb18)
- ブロック [`00afbb18`](#insn-00afbb18) 範囲 `[['00afbb18', '00afbb2b']]`
  - `CONDITIONAL_JUMP` [`00afbb28`](#insn-00afbb28) → [`00afbb3c`](#insn-00afbb3c)
  - `FALL_THROUGH` [`00afbb28`](#insn-00afbb28) → [`00afbb2c`](#insn-00afbb2c)
- ブロック [`00afbb2c`](#insn-00afbb2c) 範囲 `[['00afbb2c', '00afbb2f']]`
  - `FALL_THROUGH` [`00afbb2c`](#insn-00afbb2c) → [`00afbb30`](#insn-00afbb30)
- ブロック [`00afbb30`](#insn-00afbb30) 範囲 `[['00afbb30', '00afbb3b']]`
  - `FALL_THROUGH` [`00afbb38`](#insn-00afbb38) → [`00afbb3c`](#insn-00afbb3c)
- ブロック [`00afbb3c`](#insn-00afbb3c) 範囲 `[['00afbb3c', '00afbb4b']]`
- ブロック [`00afbb4c`](#insn-00afbb4c) 範囲 `[['00afbb4c', '00afbb53']]`
  - `CONDITIONAL_JUMP` [`00afbb50`](#insn-00afbb50) → [`00afbb18`](#insn-00afbb18)
  - `FALL_THROUGH` [`00afbb50`](#insn-00afbb50) → [`00afbb54`](#insn-00afbb54)
- ブロック [`00afbb54`](#insn-00afbb54) 範囲 `[['00afbb54', '00afbb57']]`
  - `FALL_THROUGH` [`00afbb54`](#insn-00afbb54) → [`00afbb58`](#insn-00afbb58)
- ブロック [`00afbb58`](#insn-00afbb58) 範囲 `[['00afbb58', '00afbb63']]`

## 命令位置別の参照

- [`00afbadc`](#insn-00afbadc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbae0`](#insn-00afbae0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbaec`](#insn-00afbaec) → `010a0c38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00afbaf8`](#insn-00afbaf8) → [`00afbb54`](#insn-00afbb54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbafc`](#insn-00afbafc) → [`00bdb6d0`](../00bdb/00bdb6d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb6d0` · 推定シンボル `None` · 推定型 `None`
- [`00afbb04`](#insn-00afbb04) → `010a0c40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbb08`](#insn-00afbb08) → [`00afbb4c`](#insn-00afbb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb0c`](#insn-00afbb0c) → [`00afbb4c`](#insn-00afbb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb10`](#insn-00afbb10) → [`00bdeb90`](../00bde/00bdeb90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdeb90` · 推定シンボル `None` · 推定型 `None`
- [`00afbb14`](#insn-00afbb14) → [`00afbb54`](#insn-00afbb54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb28`](#insn-00afbb28) → [`00afbb3c`](#insn-00afbb3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb3c`](#insn-00afbb3c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb50`](#insn-00afbb50) → [`00afbb18`](#insn-00afbb18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb54`](#insn-00afbb54) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb60`](#insn-00afbb60) → [`00bdeb30`](../00bde/00bdeb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdeb30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbadc`](#insn-00afbadc)

~~~json
{
  "source": "00afbadc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbae0`](#insn-00afbae0)

~~~json
{
  "source": "00afbae0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbaec`](#insn-00afbaec)

~~~json
{
  "source": "00afbaec",
  "target": "010a0c38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0c38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbaf8`](#insn-00afbaf8)

~~~json
{
  "source": "00afbaf8",
  "target": "00afbb54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbafc`](#insn-00afbafc)

~~~json
{
  "source": "00afbafc",
  "target": "00bdb6d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbb04`](#insn-00afbb04)

~~~json
{
  "source": "00afbb04",
  "target": "010a0c40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0c40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbb08`](#insn-00afbb08)

~~~json
{
  "source": "00afbb08",
  "target": "00afbb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb0c`](#insn-00afbb0c)

~~~json
{
  "source": "00afbb0c",
  "target": "00afbb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb10`](#insn-00afbb10)

~~~json
{
  "source": "00afbb10",
  "target": "00bdeb90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbb14`](#insn-00afbb14)

~~~json
{
  "source": "00afbb14",
  "target": "00afbb54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb28`](#insn-00afbb28)

~~~json
{
  "source": "00afbb28",
  "target": "00afbb3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb3c`](#insn-00afbb3c)

~~~json
{
  "source": "00afbb3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb50`](#insn-00afbb50)

~~~json
{
  "source": "00afbb50",
  "target": "00afbb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb54`](#insn-00afbb54)

~~~json
{
  "source": "00afbb54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb60`](#insn-00afbb60)

~~~json
{
  "source": "00afbb60",
  "target": "00bdeb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
