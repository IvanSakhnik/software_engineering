draw_point	proc
	push	bp
	mov	bp, sp
	mov	ax, 0A000h
	mov	es, ax
	mov	si, crt_y
	mov	di, crt_x
	cmp	si, y_res_
	jae	@nd
	cmp	di, x_res_
	jae	@nd
	mov	ax, x_res_
	mul	si
	add	ax, di
	mov	bx, ax
	mov	dx, [bp+4]
	mov	byte ptr es:[bx], dl
