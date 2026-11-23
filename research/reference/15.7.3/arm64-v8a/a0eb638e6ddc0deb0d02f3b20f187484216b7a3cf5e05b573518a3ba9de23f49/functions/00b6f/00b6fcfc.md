# 00b6fcfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b6fc34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fc34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0073.md#compare-f2606aa999f2f3dcc3aa2a2b3e7b7b8a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6fd40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6fd40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0010.md#compare-15c9091f92936ca962bf4f71abf50b86)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6fcfc",
  "name": "_ZNK8firebase4auth22AndroidWrappedUserInfo12phone_numberEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2e35f66cef5980b1d926de96e00258c3ba01185b9ec12908f6ec5de78b48e504",
  "source_text_sha256": "2e35f66cef5980b1d926de96e00258c3ba01185b9ec12908f6ec5de78b48e504",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6fcfc",
        "00b6fd7f"
      ]
    ],
    "bytes_sha256": "a92f5a65419c0820253e045818cf2a7e6a32f58e8fe96e411bef4ce5a91b6737",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bde090](../00bde/00bde090.md)
- [00bde1b0](../00bde/00bde1b0.md)
- [00bde4c0](../00bde/00bde4c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 749 bytes

~~~c

void _ZNK8firebase4auth22AndroidWrappedUserInfo12phone_numberEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  ulong uVar4;
  
  lVar1 = *(long *)(param_2 + 0xa0);
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
  lVar3 = 0;
  if (lVar1 != 0) {
    lVar3 = FUN_0047495c(uVar2,lVar1,DAT_010a1a90);
  }
  uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar2);
  if ((lVar3 != 0) && ((uVar4 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar2,lVar3);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
                    /* try { // try from 00b6fd74 to 00c6fd7b has its CatchHandler @ 00b706dc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6fcfc"></a> `00b6fcfc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b6fd00"></a> `00b6fd00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fd04"></a> `00b6fd04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6fd08"></a> `00b6fd08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b6fd0c"></a> `00b6fd0c` | `09 d4 49 a9` | ldp x9,x21,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00b6fd10"></a> `00b6fd10` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b6fd14"></a> `00b6fd14` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00b6fd18"></a> `00b6fd18` | `26 b9 01 94` | bl 0x00bde1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fd1c"></a> `00b6fd1c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6fd20"></a> `00b6fd20` | `f5 00 00 b4` | cbz x21,0x00b6fd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6fd24"></a> `00b6fd24` | `88 29 00 d0` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6fd28"></a> `00b6fd28` | `02 49 45 f9` | ldr x2,[x8, #0xa90] | `FALL_THROUGH`
<a id="insn-00b6fd2c"></a> `00b6fd2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6fd30"></a> `00b6fd30` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6fd34"></a> `00b6fd34` | `0a 13 e4 97` | bl 0x0047495c | `UNCONDITIONAL_CALL`
<a id="insn-00b6fd38"></a> `00b6fd38` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b6fd3c"></a> `00b6fd3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6fd40"></a> `00b6fd40` | `d4 b8 01 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fd44"></a> `00b6fd44` | `35 01 00 b4` | cbz x21,0x00b6fd68 | `CONDITIONAL_JUMP`
<a id="insn-00b6fd48"></a> `00b6fd48` | `00 01 00 37` | tbnz w0,#0x0,0x00b6fd68 | `CONDITIONAL_JUMP`
<a id="insn-00b6fd4c"></a> `00b6fd4c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b6fd50"></a> `00b6fd50` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6fd54"></a> `00b6fd54` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6fd58"></a> `00b6fd58` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fd5c"></a> `00b6fd5c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6fd60"></a> `00b6fd60` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6fd64"></a> `00b6fd64` | `d7 b9 01 14` | b 0x00bde4c0 | `CALL_TERMINATOR`
<a id="insn-00b6fd68"></a> `00b6fd68` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b6fd6c"></a> `00b6fd6c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fd70"></a> `00b6fd70` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6fd74"></a> `00b6fd74` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fd78"></a> `00b6fd78` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6fd7c"></a> `00b6fd7c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6fcfc`](#insn-00b6fcfc) 範囲 `[['00b6fcfc', '00b6fd23']]`
  - `CONDITIONAL_JUMP` [`00b6fd20`](#insn-00b6fd20) → [`00b6fd3c`](#insn-00b6fd3c)
  - `FALL_THROUGH` [`00b6fd20`](#insn-00b6fd20) → [`00b6fd24`](#insn-00b6fd24)
- ブロック [`00b6fd24`](#insn-00b6fd24) 範囲 `[['00b6fd24', '00b6fd3b']]`
  - `FALL_THROUGH` [`00b6fd38`](#insn-00b6fd38) → [`00b6fd3c`](#insn-00b6fd3c)
- ブロック [`00b6fd3c`](#insn-00b6fd3c) 範囲 `[['00b6fd3c', '00b6fd47']]`
  - `CONDITIONAL_JUMP` [`00b6fd44`](#insn-00b6fd44) → [`00b6fd68`](#insn-00b6fd68)
  - `FALL_THROUGH` [`00b6fd44`](#insn-00b6fd44) → [`00b6fd48`](#insn-00b6fd48)
- ブロック [`00b6fd48`](#insn-00b6fd48) 範囲 `[['00b6fd48', '00b6fd4b']]`
  - `CONDITIONAL_JUMP` [`00b6fd48`](#insn-00b6fd48) → [`00b6fd68`](#insn-00b6fd68)
  - `FALL_THROUGH` [`00b6fd48`](#insn-00b6fd48) → [`00b6fd4c`](#insn-00b6fd4c)
- ブロック [`00b6fd4c`](#insn-00b6fd4c) 範囲 `[['00b6fd4c', '00b6fd67']]`
- ブロック [`00b6fd68`](#insn-00b6fd68) 範囲 `[['00b6fd68', '00b6fd73']]`
  - `FALL_THROUGH` [`00b6fd70`](#insn-00b6fd70) → [`00b6fd74`](#insn-00b6fd74)
- ブロック [`00b6fd74`](#insn-00b6fd74) 範囲 `[['00b6fd74', '00b6fd7f']]`

## 命令位置別の参照

- [`00b6fcfc`](#insn-00b6fcfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd00`](#insn-00b6fd00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd04`](#insn-00b6fd04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd18`](#insn-00b6fd18) → [`00bde1b0`](../00bde/00bde1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd20`](#insn-00b6fd20) → [`00b6fd3c`](#insn-00b6fd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd28`](#insn-00b6fd28) → `010a1a90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6fd34`](#insn-00b6fd34) → [`0047495c`](../00474/0047495c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047495c` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd40`](#insn-00b6fd40) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd44`](#insn-00b6fd44) → [`00b6fd68`](#insn-00b6fd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd48`](#insn-00b6fd48) → [`00b6fd68`](#insn-00b6fd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd54`](#insn-00b6fd54) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd58`](#insn-00b6fd58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd64`](#insn-00b6fd64) → [`00bde4c0`](../00bde/00bde4c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde4c0` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd70`](#insn-00b6fd70) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd74`](#insn-00b6fd74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6fcfc`](#insn-00b6fcfc)

~~~json
{
  "source": "00b6fcfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd00`](#insn-00b6fd00)

~~~json
{
  "source": "00b6fd00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd04`](#insn-00b6fd04)

~~~json
{
  "source": "00b6fd04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd18`](#insn-00b6fd18)

~~~json
{
  "source": "00b6fd18",
  "target": "00bde1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fd20`](#insn-00b6fd20)

~~~json
{
  "source": "00b6fd20",
  "target": "00b6fd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd28`](#insn-00b6fd28)

~~~json
{
  "source": "00b6fd28",
  "target": "010a1a90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1a90",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6fd34`](#insn-00b6fd34)

~~~json
{
  "source": "00b6fd34",
  "target": "0047495c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fd40`](#insn-00b6fd40)

~~~json
{
  "source": "00b6fd40",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fd44`](#insn-00b6fd44)

~~~json
{
  "source": "00b6fd44",
  "target": "00b6fd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd48`](#insn-00b6fd48)

~~~json
{
  "source": "00b6fd48",
  "target": "00b6fd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd54`](#insn-00b6fd54)

~~~json
{
  "source": "00b6fd54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd58`](#insn-00b6fd58)

~~~json
{
  "source": "00b6fd58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd64`](#insn-00b6fd64)

~~~json
{
  "source": "00b6fd64",
  "target": "00bde4c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fd70`](#insn-00b6fd70)

~~~json
{
  "source": "00b6fd70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd74`](#insn-00b6fd74)

~~~json
{
  "source": "00b6fd74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
