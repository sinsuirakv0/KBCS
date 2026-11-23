# 00af8bec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00af8cb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8cb4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-6479d462dec19c22d98382a171932a5b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af8bec",
  "name": "_ZN8firebase8internal16JObjectReference3SetEP7_JNIEnvP8_jobject",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5099c55f14fd35940836c12529c39ed06d32fa32b583df20577af1fbb0ac8a92",
  "source_text_sha256": "5099c55f14fd35940836c12529c39ed06d32fa32b583df20577af1fbb0ac8a92",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af8bec",
        "00af8c9b"
      ]
    ],
    "bytes_sha256": "09403c5a8a99b307d23d9767fb216f43723e60f7caa3977c0812114072dc0dbf",
    "instruction_count": 44,
    "instruction_bytes": 176,
    "body_bytes": 176,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 959 bytes

~~~c

void _ZN8firebase8internal16JObjectReference3SetEP7_JNIEnvP8_jobject
               (undefined8 *param_1,long *param_2,long param_3)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if ((param_2 != (long *)0x0) && (param_1[1] != 0)) {
    (**(code **)(*param_2 + 0xb0))(param_2);
  }
                    /* try { // try from 00af8c34 to 00bf8c3f has its CatchHandler @ 00aff768 */
  param_1[1] = 0;
  local_40 = 0;
                    /* try { // try from 00af8c40 to 00bf8c53 has its CatchHandler @ 00aff764 */
  (**(code **)(*param_2 + 0x6d8))(param_2,&local_40);
  *param_1 = local_40;
  param_1[1] = 0;
  if (param_3 != 0) {
    uVar2 = (**(code **)(*param_2 + 0xa8))(param_2,param_3);
    param_1[1] = uVar2;
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
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
<a id="insn-00af8bec"></a> `00af8bec` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00af8bf0"></a> `00af8bf0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af8bf4"></a> `00af8bf4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af8bf8"></a> `00af8bf8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af8bfc"></a> `00af8bfc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00af8c00"></a> `00af8c00` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00af8c04"></a> `00af8c04` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00af8c08"></a> `00af8c08` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00af8c0c"></a> `00af8c0c` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00af8c10"></a> `00af8c10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af8c14"></a> `00af8c14` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00af8c18"></a> `00af8c18` | `e1 00 00 b4` | cbz x1,0x00af8c34 | `CONDITIONAL_JUMP`
<a id="insn-00af8c1c"></a> `00af8c1c` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00af8c20"></a> `00af8c20` | `a1 00 00 b4` | cbz x1,0x00af8c34 | `CONDITIONAL_JUMP`
<a id="insn-00af8c24"></a> `00af8c24` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00af8c28"></a> `00af8c28` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00af8c2c"></a> `00af8c2c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00af8c30"></a> `00af8c30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af8c34"></a> `00af8c34` | `7f 06 00 f9` | str xzr,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00af8c38"></a> `00af8c38` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00af8c3c"></a> `00af8c3c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00af8c40"></a> `00af8c40` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00af8c44"></a> `00af8c44` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00af8c48"></a> `00af8c48` | `08 6d 43 f9` | ldr x8,[x8, #0x6d8] | `FALL_THROUGH`
<a id="insn-00af8c4c"></a> `00af8c4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af8c50"></a> `00af8c50` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00af8c54"></a> `00af8c54` | `68 7e 00 a9` | stp x8,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00af8c58"></a> `00af8c58` | `f4 00 00 b4` | cbz x20,0x00af8c74 | `CONDITIONAL_JUMP`
<a id="insn-00af8c5c"></a> `00af8c5c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00af8c60"></a> `00af8c60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00af8c64"></a> `00af8c64` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00af8c68"></a> `00af8c68` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00af8c6c"></a> `00af8c6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af8c70"></a> `00af8c70` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00af8c74"></a> `00af8c74` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00af8c78"></a> `00af8c78` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00af8c7c"></a> `00af8c7c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00af8c80"></a> `00af8c80` | `c1 00 00 54` | b.ne 0x00af8c98 | `CONDITIONAL_JUMP`
<a id="insn-00af8c84"></a> `00af8c84` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af8c88"></a> `00af8c88` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af8c8c"></a> `00af8c8c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af8c90"></a> `00af8c90` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00af8c94"></a> `00af8c94` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00af8c98"></a> `00af8c98` | `be 88 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af8bec`](#insn-00af8bec) 範囲 `[['00af8bec', '00af8c1b']]`
  - `CONDITIONAL_JUMP` [`00af8c18`](#insn-00af8c18) → [`00af8c34`](#insn-00af8c34)
  - `FALL_THROUGH` [`00af8c18`](#insn-00af8c18) → [`00af8c1c`](#insn-00af8c1c)
- ブロック [`00af8c1c`](#insn-00af8c1c) 範囲 `[['00af8c1c', '00af8c23']]`
  - `CONDITIONAL_JUMP` [`00af8c20`](#insn-00af8c20) → [`00af8c34`](#insn-00af8c34)
  - `FALL_THROUGH` [`00af8c20`](#insn-00af8c20) → [`00af8c24`](#insn-00af8c24)
- ブロック [`00af8c24`](#insn-00af8c24) 範囲 `[['00af8c24', '00af8c33']]`
  - `FALL_THROUGH` [`00af8c30`](#insn-00af8c30) → [`00af8c34`](#insn-00af8c34)
- ブロック [`00af8c34`](#insn-00af8c34) 範囲 `[['00af8c34', '00af8c3f']]`
  - `FALL_THROUGH` [`00af8c3c`](#insn-00af8c3c) → [`00af8c40`](#insn-00af8c40)
- ブロック [`00af8c40`](#insn-00af8c40) 範囲 `[['00af8c40', '00af8c5b']]`
  - `CONDITIONAL_JUMP` [`00af8c58`](#insn-00af8c58) → [`00af8c74`](#insn-00af8c74)
  - `FALL_THROUGH` [`00af8c58`](#insn-00af8c58) → [`00af8c5c`](#insn-00af8c5c)
- ブロック [`00af8c5c`](#insn-00af8c5c) 範囲 `[['00af8c5c', '00af8c73']]`
  - `FALL_THROUGH` [`00af8c70`](#insn-00af8c70) → [`00af8c74`](#insn-00af8c74)
- ブロック [`00af8c74`](#insn-00af8c74) 範囲 `[['00af8c74', '00af8c83']]`
  - `CONDITIONAL_JUMP` [`00af8c80`](#insn-00af8c80) → [`00af8c98`](#insn-00af8c98)
  - `FALL_THROUGH` [`00af8c80`](#insn-00af8c80) → [`00af8c84`](#insn-00af8c84)
- ブロック [`00af8c84`](#insn-00af8c84) 範囲 `[['00af8c84', '00af8c97']]`
- ブロック [`00af8c98`](#insn-00af8c98) 範囲 `[['00af8c98', '00af8c9b']]`

## 命令位置別の参照

- [`00af8bf0`](#insn-00af8bf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8bf4`](#insn-00af8bf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8bf8`](#insn-00af8bf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8c14`](#insn-00af8c14) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8c18`](#insn-00af8c18) → [`00af8c34`](#insn-00af8c34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8c20`](#insn-00af8c20) → [`00af8c34`](#insn-00af8c34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8c38`](#insn-00af8c38) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8c50`](#insn-00af8c50) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8c58`](#insn-00af8c58) → [`00af8c74`](#insn-00af8c74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8c78`](#insn-00af8c78) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8c80`](#insn-00af8c80) → [`00af8c98`](#insn-00af8c98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8c84`](#insn-00af8c84) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8c88`](#insn-00af8c88) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8c8c`](#insn-00af8c8c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8c98`](#insn-00af8c98) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af8bf0`](#insn-00af8bf0)

~~~json
{
  "source": "00af8bf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8bf4`](#insn-00af8bf4)

~~~json
{
  "source": "00af8bf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8bf8`](#insn-00af8bf8)

~~~json
{
  "source": "00af8bf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8c14`](#insn-00af8c14)

~~~json
{
  "source": "00af8c14",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8c18`](#insn-00af8c18)

~~~json
{
  "source": "00af8c18",
  "target": "00af8c34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8c20`](#insn-00af8c20)

~~~json
{
  "source": "00af8c20",
  "target": "00af8c34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8c38`](#insn-00af8c38)

~~~json
{
  "source": "00af8c38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8c50`](#insn-00af8c50)

~~~json
{
  "source": "00af8c50",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8c58`](#insn-00af8c58)

~~~json
{
  "source": "00af8c58",
  "target": "00af8c74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8c78`](#insn-00af8c78)

~~~json
{
  "source": "00af8c78",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8c80`](#insn-00af8c80)

~~~json
{
  "source": "00af8c80",
  "target": "00af8c98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8c84`](#insn-00af8c84)

~~~json
{
  "source": "00af8c84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8c88`](#insn-00af8c88)

~~~json
{
  "source": "00af8c88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8c8c`](#insn-00af8c8c)

~~~json
{
  "source": "00af8c8c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8c98`](#insn-00af8c98)

~~~json
{
  "source": "00af8c98",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
